from dataclasses import dataclass, field
from typing import List
from Lock import Lock
from Player import Player


@dataclass
class Cave:
    """
    The Cave class manages:
    - Oxygen levels per cave level
    - Lethality per cave level
    - Locks (doors) for each cave

    Rules:
    - Each cave has increasing lethality: 0.2, 0.3, 0.4
    - If oxygen reaches zero, all players die and lose the game
    - If a player dies because their gems die, cave lethality is reduced by half
    - Leaving the third cave ends the game
    """

    locks: List[Lock] = field(default_factory=list)
    oxygen_levels: List[float] = field(default_factory=list)
    lethality_levels: List[float] = field(default_factory=list)

    # -------------------------------------------------------------
    # Constructor (equivalent to Java no-arg constructor)
    # -------------------------------------------------------------
    def __post_init__(self):
        if not self.locks:
            lock_names = ["1", "2", "3"]

            self.lethality_levels = [0.2, 0.3, 0.4]
            self.oxygen_levels = [1.0, 1.0, 1.0]

            self.locks = [
                Lock(f"Cave {lock_name}")
                for lock_name in lock_names
            ]

    # -------------------------------------------------------------
    # Oxygen handling
    # -------------------------------------------------------------
    def set_player_oxygen(self, player: Player, oxygen: float, cave_index: int):
        """
        Updates the oxygen for a specific cave
        and applies it to the player.

        cave_index:
        1 = Cave 1
        2 = Cave 2
        3 = Cave 3
        """
        self.oxygen_levels[cave_index - 1] = oxygen
        player.oxygen_level = self.oxygen_levels[cave_index - 1]

    def decrease_cave_oxygen(self, cave_index: int, amount: float):
        """
        Decreases oxygen for a specific cave.
        """
        self.oxygen_levels[cave_index - 1] -= amount

    def get_cave_oxygen(self, cave_index: int) -> float:
        """
        Returns oxygen level of a cave.
        """
        return self.oxygen_levels[cave_index - 1]

    # -------------------------------------------------------------
    # Lock handling
    # -------------------------------------------------------------
    def get_lock(self, lock_index: int) -> Lock:
        """
        Returns the selected lock:
        1 = Lock 1
        2 = Lock 2
        3 = Lock 3 (default)
        """
        if lock_index == 1:
            return self.locks[0]
        elif lock_index == 2:
            return self.locks[1]
        return self.locks[2]

    def set_lock(self, lock: Lock, lock_index: int):
        """
        Assigns a lock to a cave position.
        """
        if lock_index == 1:
            self.locks[0] = lock
        elif lock_index == 2:
            self.locks[1] = lock
        else:
            self.locks[2] = lock

    # -------------------------------------------------------------
    # Lethality handling
    # -------------------------------------------------------------
    def set_lethality(self, lethality: float, cave_index: int):
        """
        Sets lethality for a cave.
        """
        self.lethality_levels[cave_index - 1] = lethality

    def get_lethality(self, cave_index: int) -> float:
        """
        Returns lethality for a cave.
        """
        return self.lethality_levels[cave_index - 1]

    # -------------------------------------------------------------
    # String representations
    # -------------------------------------------------------------
    def cave_status(self, cave_index: int) -> str:
        """
        Displays cave information during gameplay.
        """
        return (
            f"--Cave: {self.locks[cave_index - 1].name}--\t"
            f"--Lethality: {self.lethality_levels[cave_index - 1] * 100:.0f}%--\t"
            f"--Oxygen: {self.oxygen_levels[cave_index - 1] * 100:.0f}%--\n"
        )

    def __str__(self) -> str:
        """
        Displays full cave information at the end of the game.
        """
        summary = ""

        for i in range(3):
            summary += (
                f"--Cave: {self.locks[i].name}--\t"
                f"--Lethality: {self.lethality_levels[i]}--\t"
                f"--Oxygen: {self.oxygen_levels[i]}--\n\n"
            )

            for gem in self.locks[i].gems:
                summary += f"{gem}\n"

            summary += "\n"

        return summary
