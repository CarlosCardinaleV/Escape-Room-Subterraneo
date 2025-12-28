from dataclasses import dataclass, field
from typing import List
from Player import Player


@dataclass
class Team:
    """
    Team creates a group of three players and assigns a team name.
    """
    _name: str = "Team #"
    players: List["Player"] = field(default_factory=lambda: [Player() for _ in range(3)])
    _alive: bool = True

    # -------------------------
    # Properties
    # -------------------------

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def alive(self) -> bool:
        return self._alive

    @alive.setter
    def alive(self, value: bool) -> None:
        self._alive = value

    # -------------------------
    # Player access
    # -------------------------

    def get_player(self, index: int):
        """
        1 -> player 1
        2 -> player 2
        3 -> player 3 (any other value returns player 3)
        """
        if index == 1:
            return self.players[0]
        elif index == 2:
            return self.players[1]
        else:
            return self.players[2]

    def set_player(self, player, index: int) -> None:
        self.players[index] = player

    # -------------------------
    # Computed properties
    # -------------------------

    @property
    def alive_players_count(self) -> int:
        return sum(player.vida for player in self.players)

    # -------------------------
    # String representations
    # -------------------------

    def to_string_team(self) -> str:
        """
        Used while the game is still running.
        """
        info = (
            f"Team name: {self.name}\t"
            f"Alive players: {self.alive_players_count}\n"
            "Players:\t"
        )

        info += "    ".join(player.nombre for player in self.players)
        info += "\n\n"

        for player in self.players:
            info += player.to_string_jugador()

        return info

    def __str__(self) -> str:
        """
        Used when the game ends.
        """
        info = (
            f"\nTeam name: {self.name}\n"
            f"Alive players: {self.alive_players_count}\n"
            "Players:\t"
        )

        info += "\t".join(player.nombre for player in self.players)
        info += "\n"

        for player in self.players:
            for i in range(3):
                info += str(player.gemas[i]) + "\n"
            info += "\n"

        return info

    # -------------------------
    # Display
    # -------------------------

    def display_team(self) -> None:
        print(f"Team name: {self.name}")
        print(f"Alive players: {self.alive_players_count}")
        print("Players:\n")

        for player in self.players:
            print(f"{player.nombre} -->\t", end="")
            for gem in player.gemas:
                print(gem.to_string_gema(), end="\t")
            print()
