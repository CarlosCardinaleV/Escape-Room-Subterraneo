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

    gem_type: str = field(default=None)
    owner: str = field(default=None)
    health: float = field(default=1.0)
    attack: float = field(default=0.0)
    defense: float = field(default=0.0)

    # -------------------------------------------------------------
    # Constructors (replacement for Java overloads)
    # -------------------------------------------------------------

    @classmethod
    def with_all(cls, gem_type: str, owner: str, attack: float, defense: float):
        """Equivalent to the Java constructor with all parameters."""
        return cls(gem_type=gem_type, owner=owner, health=1.0, attack=attack, defense=defense)

    @classmethod
    def random_for_cave(cls, cave_name: str = "Cave #"):
        """Creates a random gem for the cave."""
        gem_type = random.choice(["FIRE", "WATER", "METAL"])
        attack = num_random(0.6, 1.0)
        defense = num_random(0.1, 0.5)
        return cls(gem_type=gem_type, owner=cave_name, health=1.0, attack=attack, defense=defense)

    @classmethod
    def for_player(cls, owner: str, gem_type: str):
        """Creates a gem for a player with a selected type."""
        attack = num_random(0.6, 1.0)
        defense = num_random(0.1, 0.5)
        return cls(gem_type=gem_type, owner=owner, health=1.0, attack=attack, defense=defense)

    @classmethod
    def random_with_owner(cls, owner: str):
        """Creates a random-type gem assigned to a specific owner."""
        gem_type = random.choice(["FIRE", "WATER", "METAL"])
        attack = num_random(0.6, 1.0)
        defense = num_random(0.1, 0.5)
        return cls(gem_type=gem_type, owner=owner, health=1.0, attack=attack, defense=defense)

    # -------------------------------------------------------------
    # Properties (replacement for Java getters and setters)
    # -------------------------------------------------------------

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        # Health cannot be negative
        self._health = max(0.0, value)

    # -------------------------------------------------------------
    # Display / toString equivalents
    # -------------------------------------------------------------

    def __str__(self):
        """Detailed information about the gem."""
        return (
            f"Gem owned by: {self.owner}\n"
            f"Health: {self.health}\n"
            f"Attack: {self.attack}\n"
            f"Defense: {self.defense}\n"
            f"Gem Type: {self.gem_type}\n"
        )

    def summary(self):
        """Short version (equivalent to Java's toStringGema)."""
        return f"{self.gem_type}: {self.health * 100:.1f}%"

    def display(self):
        """Prints gem information."""
        print(self)
