from dataclasses import dataclass, field
from typing import List
from Gem import Gem

@dataclass
class Lock:
    """
    The Lock class creates three random gems for each lock (cave door).
    Each gem has a random type, attack, defense, and is assigned
    to the door/lock it belongs to.
    """

    name: str = "Lock #"
    gems: List[Gem] = field(default_factory=List)
    health: float = 1.0
    destroyed: bool = False

    # ---------------------------------------------------------------
    # Post-initialization (equivalent to Java constructors)
    # ---------------------------------------------------------------
    def __post_init__(self):
        # if gems are not manually provided, create three random gems
        if not self.gems:
            self.gems = [
                Gem.random_for_cave(self.name)
                for _ in range(3)
            ]

    # ---------------------------------------------------------------
    # Properties for alive state
    # ---------------------------------------------------------------
    @property
    def is_alive(self) -> bool:
        return self.is_alive

    @is_alive.setter
    def is_alive(self, value: bool):
        self.alive = value
    
    # ---------------------------------------------------------------
    # Gem access and modification
    # ---------------------------------------------------------------
    def get_gem(self, index: int) -> Gem:
        """Returns the selected gem:
        1=Fire
        2=Water
        3=Metal (default for any other interger)"""
        if index == 1:
            return self.gems[0]
        elif index == 2:
            return self.gems[1]
        return self.gems[2]
    
    def set_gem_health(self, index: int, health: float):
        """
        Sets the health of a specific gem.
        Used by the Spell class.
        """
        gem = self.get_gem(index)
        gem.health = health

    # -------------------------------------------------------------
    # Lock health
    # -------------------------------------------------------------
    @property
    def lock_health(self) -> float:
        return self.health

    @lock_health.setter
    def lock_health(self, value: float):
        self.health = value

    # -------------------------------------------------------------
    # String representations
    # -------------------------------------------------------------
    def __str__(self):
        """Full lock information (used at end of game)."""
        info = (
            f"Lock: {self.name}\n"
            f"Lock Health Percentage: {self.health}\n"
            f"Gems:\n"
        )
        for gem in self.gems:
            info += str(gem) + "\n"
        return info

    def short_status(self):
        """Simplified information shown during gameplay."""
        info = (
            f"Lock: {self.name}\n"
            f"Gems:\n"
            f"First Gem: {self.gems[0].health * 100:.1f}%   "
            f"Second Gem: {self.gems[1].health * 100:.1f}%   "
            f"Third Gem: {self.gems[2].health * 100:.1f}%\n"
        )
        return info

    def display(self):
        """Prints full lock information."""
        print(f"Level: {self.name}")
        print(f"Lock Health Percentage: {self.health}")
        print("Gems:")
        for gem in self.gems:
            print(gem)