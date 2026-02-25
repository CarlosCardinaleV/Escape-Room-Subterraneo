from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Tuple

from Cave import Cave
from Lock import Lock
from Player import Player
from Team import Team


@dataclass
class ScapeRoomConsole:
    """
    Console game runner for Underground Escape Room using the current dataclass API.
    """

    best_team_name: Optional[str] = None
    best_cave_reached: int = 0
    teams: List[Team] = field(default_factory=list)
    caves: List[Cave] = field(default_factory=list)

    def run(self) -> None:
        team_count = self._ask_int(
            "How many teams will play Underground Escape Room? ", minimum=1
        )

        for team_idx in range(team_count):
            team, cave = self._build_team_and_cave(team_idx)
            self.teams.append(team)
            self.caves.append(cave)

            dead_players_count = 0
            first_death_applied = False
            second_death_applied = False

            choice = self._initial_menu(team, cave, team_idx + 1, spell_count=0)
            if choice == 2:
                print("\nTeam abandoned before entering Cave 1.")
                continue

            # Java-style flow: 3 caves, one lock per cave.
            for cave_idx in range(3):
                status, dead_players_count, first_death_applied, second_death_applied = self._play_cave(
                    team=team,
                    cave=cave,
                    cave_idx=cave_idx,
                    dead_players_count=dead_players_count,
                    first_death_applied=first_death_applied,
                    second_death_applied=second_death_applied,
                )

                if status == "lose":
                    break

                if status == "abandon":
                    print("\nTeam abandoned the run.")
                    break

                # status == "cleared"
                self._update_best_progress(team, cave_idx + 1)

                if cave_idx == 2:
                    print("\nCongratulations! Team cleared all caves.")
                    print(team)
                    break

                choice = self._ask_int(
                    "\n1. Continue to next cave\n2. Abandon game\nChoose: "
                )
                if choice == 2:
                    print("\nTeam abandoned after clearing a cave.")
                    break

    def _build_team_and_cave(self, team_number: int) -> Tuple[Team, Cave]:
        team_name = input(f"\nTeam name {team_number + 1}: ").strip() or f"Team {team_number + 1}"

        players: List[Player] = []
        for player_idx in range(3):
            player_name = input(f"Player name {player_idx + 1}: ").strip() or f"Player {player_idx + 1}"
            players.append(Player.with_name(player_name))

        team = Team.with_name(team_name)
        for idx, player in enumerate(players):
            team.set_player(player, idx)

        cave = Cave()
        return team, cave

    def _initial_menu(self, team: Team, cave: Cave, cave_number: int, spell_count: int) -> int:
        summary = (
            f"\nGame summary:\n"
            f"{cave.cave_status(cave_number - 1)}"
            f"Spells cast: {spell_count}\n"
            f"{team.to_string_team()}\n"
            "1. Cast spell\n"
            "2. Abandon game\n"
            "3. Best team so far\n"
        )

        choice = self._ask_int(summary + "Choose: ")

        if choice == 3:
            if self.best_team_name:
                print(
                    "\nBest team so far:\n"
                    f"{self.best_team_name} (cleared {self.best_cave_reached} cave(s))"
                )
            else:
                print("\nNo progress history yet.")
            choice = self._ask_int("\n1. Continue\n2. Abandon\nChoose: ")

        return choice

    def _play_cave(
        self,
        team: Team,
        cave: Cave,
        cave_idx: int,
        dead_players_count: int,
        first_death_applied: bool,
        second_death_applied: bool,
    ) -> Tuple[str, int, bool, bool]:
        lock = cave.get_lock(cave_idx)
        spell_count = 0

        base_lethality = [0.2, 0.3, 0.4][cave_idx]
        cave.set_lethality(base_lethality, cave_idx)

        while team.alive and cave.get_cave_oxygen(cave_idx) > 0.0 and not lock.is_destroyed:
            print("\n" + "=" * 60)
            print(
                f"Cave {cave_idx + 1} | Oxygen: {cave.get_cave_oxygen(cave_idx) * 100:.1f}%"
            )
            print(lock.short_status())

            spell_seconds = self._ask_float("Spell duration in seconds (>=1.0): ", minimum=1.0)

            for player in team.players:
                if not player.is_alive:
                    continue

                print(player.short_status())
                player_gem_choice = self._ask_int("Choose player gem (1 FIRE, 2 WATER, 3 METAL): ", 1, 3)
                lock_gem_choice = self._ask_int("Choose lock gem (1, 2, 3): ", 1, 3)

                self._resolve_combat(player, lock, player_gem_choice, lock_gem_choice, spell_seconds)

                if self._all_player_gems_dead(player):
                    player.is_alive = False
                    dead_players_count += 1
                    print(f"{player.name} has fallen. All gems are depleted.")

            spell_count += 1

            if dead_players_count >= 1 and not first_death_applied:
                cave.set_lethality(base_lethality / 2.0, cave_idx)
                first_death_applied = True

            if dead_players_count >= 2 and not second_death_applied:
                cave.set_lethality(base_lethality / 4.0, cave_idx)
                second_death_applied = True

            cave.decrease_cave_oxygen(cave_idx, cave.get_lethality(cave_idx))

            if cave.get_cave_oxygen(cave_idx) <= 0.0:
                team.alive = False
                print("\nGAME OVER: the team ran out of oxygen.")
                print(team)
                print(cave)
                return "lose", dead_players_count, first_death_applied, second_death_applied

            if all(not player.is_alive for player in team.players):
                team.alive = False
                print("\nGAME OVER: all players are dead.")
                print(team)
                print(cave)
                return "lose", dead_players_count, first_death_applied, second_death_applied

            if self._all_lock_gems_dead(lock):
                lock.is_destroyed = True
                print(
                    f"\nCave {cave_idx + 1} cleared. "
                    f"Spells cast in this cave: {spell_count}"
                )
                return "cleared", dead_players_count, first_death_applied, second_death_applied

            next_choice = self._ask_int(
                "\n1. Cast another spell\n2. Abandon game\nChoose: ", 1, 2
            )
            if next_choice == 2:
                return "abandon", dead_players_count, first_death_applied, second_death_applied

        return "lose", dead_players_count, first_death_applied, second_death_applied

    def _update_best_progress(self, team: Team, cave_reached: int) -> None:
        if cave_reached > self.best_cave_reached:
            self.best_cave_reached = cave_reached
            self.best_team_name = team.name

    def _resolve_combat(
        self,
        player: Player,
        lock: Lock,
        player_gem_index: int,
        lock_gem_index: int,
        seconds: float,
    ) -> None:
        player_gem = player.get_gem(player_gem_index)
        lock_gem = lock.get_gem(lock_gem_index)

        atk_p = player_gem.attack
        def_p = player_gem.defense
        type_p = player_gem.gem_type

        atk_l = lock_gem.attack
        def_l = lock_gem.defense
        type_l = lock_gem.gem_type

        dmg_to_player = max(0.0, (atk_l - def_p) * seconds)
        dmg_to_lock = max(0.0, (atk_p - def_l) * seconds)

        if type_p == type_l:
            player.set_gem_health(player_gem_index, player_gem.health - dmg_to_player)
            lock.set_gem_health(lock_gem_index, lock_gem.health - dmg_to_lock)
            return

        # Type advantage mapping from original Java logic:
        # FIRE > METAL, METAL > WATER, WATER > FIRE.
        if (type_p, type_l) in {
            ("FIRE", "METAL"),
            ("METAL", "WATER"),
            ("WATER", "FIRE"),
        }:
            lock.set_gem_health(lock_gem_index, lock_gem.health - dmg_to_lock)
        else:
            player.set_gem_health(player_gem_index, player_gem.health - dmg_to_player)

    @staticmethod
    def _all_player_gems_dead(player: Player) -> bool:
        return all(player.get_gem(i).health <= 0.0 for i in (1, 2, 3))

    @staticmethod
    def _all_lock_gems_dead(lock: Lock) -> bool:
        return all(lock.get_gem(i).health <= 0.0 for i in (1, 2, 3))

    @staticmethod
    def _ask_int(prompt: str, minimum: Optional[int] = None, maximum: Optional[int] = None) -> int:
        while True:
            raw = input(prompt).strip()
            try:
                value = int(raw)
            except ValueError:
                print("Please enter a valid integer.")
                continue

            if minimum is not None and value < minimum:
                print(f"Value must be >= {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Value must be <= {maximum}.")
                continue

            return value

    @staticmethod
    def _ask_float(prompt: str, minimum: Optional[float] = None) -> float:
        while True:
            raw = input(prompt).strip()
            try:
                value = float(raw)
            except ValueError:
                print("Please enter a valid number.")
                continue

            if minimum is not None and value < minimum:
                print(f"Value must be >= {minimum}.")
                continue

            return value


if __name__ == "__main__":
    ScapeRoomConsole().run()
