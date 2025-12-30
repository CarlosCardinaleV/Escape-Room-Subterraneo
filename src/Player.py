from dataclasses import dataclass, field
from typing import List
from Gem import Gem


@dataclass
class Player:
    """
    The Player class creates three gems (FIRE, WATER, METAL)
    and assigns the player name to each one.
    """
    _name: str = field(default="Player #")
    _gems: List[Gem] = field(default_factory=list)
    _oxygen: float = 1.0
    _alive: bool = True

    def __post_init__(self):
        # If gems were not manually provided, create three default gems
        if not self._gems:
            gem_types = ["FIRE", "WATER", "METAL"]
            self._gems = [
                Gem.for_player(self._name, gem_type)
                for gem_type in gem_types
            ]

    @classmethod
    def with_name(cls, name: str):
        """Creates a player with a specific name."""
        return cls(_name=name)

    # Gem access methods
    def get_gem(self, index: int) -> Gem:
        """
        Returns the selected gem:
        1 = FIRE
        2 = WATER
        3 = METAL (default for any other integer)
        """
        if index == 1:
            return self._gems[0]
        elif index == 2:
            return self._gems[1]
        return self._gems[2]

    def set_gem_health(self, index: int, health: float):
        """
        Sets the health of the selected gem.
        Used by the Spell class in the original Java project.
        """
        gem = self.get_gem(index)
        gem._health = health

    @property
    def gems(self) -> List[Gem]:
        """Returns the list of gems owned by the player."""
        return self._gems

    # Properties for name, oxygen, alive
    @property
    def name(self) -> str:
        """Returns the name of the player."""
        return self._name

    @name.setter
    def name(self, value: str):
        """Sets the name of the player."""
        self._name = value

    @property
    def is_alive(self) -> bool:
        """Returns whether the player is alive."""
        return self._alive
    
    @is_alive.setter
    def is_alive(self, value: bool):
        """Sets the alive status of the player."""
        self._alive = value
    
    @property
    def oxygen_level(self) -> float:
        """Returns the oxygen level of the player."""
        return self._oxygen
    
    @oxygen_level.setter
    def oxygen_level(self, value: float):
        """Sets the oxygen level of the player."""
        self._oxygen = value

    # String representations
    def __str__(self):
        """Full player information, used at the end of the game."""
        info = (
            f"\nPlayer Name: {self._name}\n"
            f"Oxygen Level: {self._oxygen}\n"
            f"Life status: {'alive' if self._alive else 'dead'}\n"
            f"Gems:\n"
        )
        for gem in self._gems:
            info += str(gem) + "\n"
        return info

    def short_status(self):
        """Simplified info shown during gameplay."""
        info = (
            f"\nPlayer Name: {self._name}\t"
            f"Life status: {'alive' if self._alive else 'dead'}\n"
            f"Gems ->"
        )
        for gem in self._gems:
            info += f"  {gem.summary()}\t"
        return info

    def display(self):
        """Prints all player information."""
        print(f"Player Name: {self._name}")
        print(f"Oxygen: {self._oxygen}")
        print(f"Life status: {'alive' if self._alive else 'dead'}")
        print("Gems:")
        for gem in self._gems:
            print(gem)
