from dataclasses import dataclass, field
from typing import List
from Gem import Gem


@dataclass
class Player:
    """
    The Player class creates three gems (FIRE, WATER, METAL)
    and assigns the player name to each one.
    """

    name: str = "Player #"
    gems: List[Gem] = field(default_factory=list)
    oxygen: float = 1.0
    alive: bool = True
    health: float = 1.0

    def __post_init__(self):
        # If gems were not manually provided, create three default gems
        if not self.gems:
            gem_types = ["FIRE", "WATER", "METAL"]
            self.gems = [
                Gem.for_player(self.name, gem_type)
                for gem_type in gem_types
            ]

    # -------------------------------------------------------------
    # Alternative constructor (equivalent to Java constructor w/ name)
    # -------------------------------------------------------------
    @classmethod
    def with_name(cls, name: str):
        return cls(name=name)

    # -------------------------------------------------------------
    # Gem access methods (replicating Java behavior)
    # -------------------------------------------------------------
    def get_gem(self, index: int) -> Gem:
        """
        Returns the selected gem:
        1 = FIRE
        2 = WATER
        3 = METAL (default for any other integer)
        """
        if index == 1:
            return self.gems[0]
        elif index == 2:
            return self.gems[1]
        return self.gems[2]

    def set_gem_health(self, index: int, health: float):
        """
        Sets the health of the selected gem.
        Used by the Spell class in the original Java project.
        """
        gem = self.get_gem(index)
        gem.health = health

    # -------------------------------------------------------------
    # Properties for name, oxygen, alive (clean Python style)
    # -------------------------------------------------------------
    @property
    def is_alive(self) -> bool:
        return self.alive

    @is_alive.setter
    def is_alive(self, value: bool):
        self.alive = value

    @property
    def oxygen_level(self) -> float:
        return self.oxygen

    @oxygen_level.setter
    def oxygen_level(self, value: float):
        self.oxygen = value

    # -------------------------------------------------------------
    # String representations (equivalent to Java toString methods)
    # -------------------------------------------------------------
    def __str__(self):
        """Full player information, used at the end of the game."""
        info = (
            f"\nPlayer Name: {self.name}\n"
            f"Oxygen Level: {self.oxygen}\n"
            f"Alive? {self.alive}\n"
            f"Gems:\n"
        )
        for gem in self.gems:
            info += str(gem) + "\n"
        return info

    def short_status(self):
        """Simplified info shown during gameplay."""
        info = (
            f"\nPlayer Name: {self.name}\t"
            f"Alive? {self.alive}\n"
            f"Gems:\t"
        )
        for gem in self.gems:
            info += f"  {gem.summary()}\t"
        return info

    def display(self):
        """Prints all player information."""
        print(f"Player Name: {self.name}")
        print(f"Oxygen: {self.oxygen}")
        print(f"Alive? {self.alive}")
        print("Gems:")
        for gem in self.gems:
            print(gem)



player1 = Player.with_name("Carlos")

print(player1.short_status())
player1.set_gem_health(1, 0.7)
player1.set_gem_health(2, 0.9)
print('-'*80)
print(player1)
