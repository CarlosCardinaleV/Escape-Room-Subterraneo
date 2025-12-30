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

    def __post_init__(self):
        # If players were not manually provided, create three default players
        if not self.players:
            self.players = [Player() for _ in range(3)]

    @classmethod
    def with_name(cls, name: str):
        """Creates a team with a specific name."""
        return cls(_name=name)

    @property
    def name(self) -> str:
        """Returns the name of the team."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Sets the name of the team."""
        self._name = value

    @property
    def alive(self) -> bool:
        """Returns whether the team is alive."""
        return self._alive

    @alive.setter
    def alive(self, value: bool) -> None:
        """Sets the alive status of the team."""
        self._alive = value


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
        """Sets a player at the specified index (0, 1, or 2)."""
        self.players[index] = player

    @property
    def alive_players_count(self) -> int:
        """Returns the count of alive players in the team."""
        return sum(player.is_alive for player in self.players)

    def to_string_team(self) -> str:
        """
        Used while the game is still running. Provides a brief status of the team and its players.
        """
        info = (
            f"Team name: {self.name}\t"
            f"Alive players: {self.alive_players_count}\n"
            "Players:\t"
        )

        info += "    ".join(player.name for player in self.players)
        info += "\n\n"

        for player in self.players:
            info += player.short_status()

        return info

    def __str__(self) -> str:
        """
        Used when the game ends. Provides full details of the team and its players.
        """
        info = (
            f"\nTeam name: {self.name}\n"
            f"Alive players: {self.alive_players_count}\n"
            "Players:\t"
        )

        info += "\t".join(player.name for player in self.players)
        info += "\n"

        for player in self.players:
            for i in range(3):
                info += str(player.gems[i]) + "\n"
            info += "\n"

        return info

    def display_team(self) -> None:
        """Prints a summary of the team and its players' gems."""
        print(f"Team name: {self.name}")
        print(f"Alive players: {self.alive_players_count}")
        print("\nPlayers:")

        for player in self.players:
            print(f"{player.name} -->\t", end="")
            for gem in player.gems:
                print(gem.summary(), end="\t")
            print()

# player1 = Player.with_name("Alice")
# player2 = Player.with_name("Bob")
# player3 = Player.with_name("Charlie")
# team = Team.with_name("Explorers")
# team.set_player(player1, 0)
# team.set_player(player2, 1)
# team.set_player(player3, 2)
# team.players[0].set_gem_health(1, 0.75)
# team.players[1].set_gem_health(2, 0.50)
# team.players[2].set_gem_health(3, 0.25)
# print(team.display_team())
# print(team.to_string_team())