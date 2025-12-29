import random
from dataclasses import dataclass, field

def num_random(min_value: float, max_value: float) -> float:
    """Returns a random float within a given range."""
    return random.uniform(min_value, max_value)


@dataclass
class Gem:
    """
    Represents a magical gem with attributes:
    - type: FIRE, WATER, METAL
    - owner: name of the player or cave
    - health: default 1.0
    - attack: random between 0.6 and 1.0
    - defense: random between 0.1 and 0.5
    """

    _gem_type: str = field(default=None)
    _owner: str = field(default=None)
    _health: float = field(default=1.0)
    _attack: float = field(default=0.0)
    _defense: float = field(default=0.0)

    # Constructors for cave
    @classmethod
    def random_for_cave(cls, cave_name: str = "Cave #"):
        """Creates a random gem for the cave."""
        gem_type = random.choice(["FIRE", "WATER", "METAL"])
        attack = num_random(0.6, 1.0)
        defense = num_random(0.1, 0.5)
        return cls(_gem_type=gem_type, _owner=cave_name, _health=1.0, _attack=attack, _defense=defense)

    # constructors for player
    @classmethod
    def for_player(cls, owner: str, gem_type: str):
        """Creates a gem for a player with a selected type."""
        attack = num_random(0.6, 1.0)
        defense = num_random(0.1, 0.5)
        return cls(_gem_type=gem_type, _owner=owner, _health=1.0, _attack=attack, _defense=defense)

    # Properties for gem attributes
    @property
    def health(self):
        """Returns the health of the gem."""
        return self._health
    @property
    def owner(self):
        """Returns the owner of the gem."""
        return self._owner
    @property
    def gem_type(self):
        """Returns the type of the gem."""
        return self._gem_type
    @property
    def attack(self):
        """Returns the attack value of the gem."""
        return self._attack
    @property
    def defense(self):
        """Returns the defense value of the gem."""
        return self._defense
    
    # Setter for health
    @health.setter
    def health(self, value):
        """Sets the health of the gem."""
        # Health cannot be negative
        self._health = max(0.0, value)

    # Display / toString equivalents
    def __str__(self):
        """Detailed information about the gem."""
        return (
            f"Gem owned by: {self._owner}\n"
            f"Health: {self._health}\n"
            f"Attack: {self._attack}\n"
            f"Defense: {self._defense}\n"
            f"Type: {self._gem_type}\n"
        )

    def summary(self):
        """Short version of gem information."""
        return f"{self._gem_type} : {self._health * 100:.1f}%"

    def display(self):
        """Prints gem information."""
        print(self)
