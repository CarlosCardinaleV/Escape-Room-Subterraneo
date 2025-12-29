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
    _name: str = "Lock #"
    _gems: List[Gem] = field(default_factory=List)
    _health: float = 1.0
    _destroyed: bool = False

    # Post-initialization
    def __post_init__(self):
        # if gems are not manually provided, create three random gems
        if not self._gems:
            self._gems = [
                Gem.random_for_cave(self._name)
                for _ in range(3)
            ]

    @classmethod
    def for_lock(cls, name: str):
        """Creates a lock with three random gems."""
        return cls(_name=name)

    @property
    def is_destroyed(self) -> bool:
        """Returns whether the lock is destroyed."""
        return self._destroyed

    @is_destroyed.setter
    def is_destroyed(self, value: bool):
        """Sets the destroyed status of the lock."""
        self._destroyed = value

    # Gem access and modification
    def get_gem(self, index: int) -> Gem:
        """Returns the selected gem:
        1=Fire
        2=Water
        3=Metal (default for any other interger)"""
        if index == 1:
            return self._gems[0]
        elif index == 2:
            return self._gems[1]
        return self._gems[2]
    
    def set_gem_health(self, index: int, health: float):
        """
        Sets the health of a specific gem.
        Used by the Spell class.
        """
        gem = self.get_gem(index)
        gem._health = health

    # Lock health property
    @property
    def lock_health(self) -> float:
        """Returns the health of the lock."""
        return self._health

    @lock_health.setter
    def lock_health(self, value: float):
        """Sets the health of the lock."""
        self._health = value

    # String representations
    def __str__(self):
        """Full lock information (used at end of game)."""
        info = (
            f"Lock: {self._name}\n"
            f"Lock Health Percentage: {self._health}\n"
            f"Gems:\n"
        )
        for gem in self._gems:
            info += str(gem) + "\n"
        return info

    def short_status(self):
        """Simplified information shown during gameplay."""
        info = (
            f"Lock: {self._name}\n"
            f"Gems:\n"
            f"First Gem: {self._gems[0]._health * 100:.1f}%   "
            f"Second Gem: {self._gems[1]._health * 100:.1f}%   "
            f"Third Gem: {self._gems[2]._health * 100:.1f}%\n"
        )
        return info

    def display(self):
        """Prints full lock information."""
        print(f"Level: {self._name}")
        print(f"Lock Health Percentage: {self._health}")
        print("Gems:")
        for gem in self._gems:
            print(gem)

cave_lock = Lock.for_lock("Cave Entrance")
cave_lock.display()