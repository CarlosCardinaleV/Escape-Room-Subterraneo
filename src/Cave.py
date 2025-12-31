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

    _locks: List[Lock] = field(default_factory=list)
    _oxygen_levels: List[float] = field(default_factory=list)
    _lethality_levels: List[float] = field(default_factory=list)

    def __post_init__(self):
        if not self._locks:
            lock_names = ["Dragon Entrance", "Crystal Abyss", "Whispering Grotto"]

            self._lethality_levels = [0.2, 0.3, 0.4]
            self._oxygen_levels = [1.0, 1.0, 1.0]

            self._locks = [
                Lock(f"Cave {lock_name}")
                for lock_name in lock_names
            ]

    def set_player_oxygen(self, player: Player, oxygen: float, cave_index: int):
        """
        Updates the oxygen for a specific cave
        and applies it to the player.

        cave_index:
        0 = Cave 1
        1 = Cave 2
        2 = Cave 3
        """
        self._oxygen_levels[cave_index] = oxygen
        player.oxygen_level = self._oxygen_levels[cave_index]

    def decrease_cave_oxygen(self, cave_index: int, amount: float):
        """
        Decreases oxygen for a specific cave.
        cave_index:
        0 = Cave 1
        1 = Cave 2
        2 = Cave 3
        """
        self._oxygen_levels[cave_index] -= amount

    def get_cave_oxygen(self, cave_index: int) -> float:
        """
        Returns oxygen level of a cave.
        cave_index:
        0 = Cave 1
        1 = Cave 2
        2 = Cave 3
        """
        return self._oxygen_levels[cave_index]

    def get_lock(self, lock_index: int) -> Lock:
        """
        Returns the selected lock:
        0 = Lock 1
        1 = Lock 2
        2 = Lock 3 (default)
        """
        if lock_index == 0:
            return self._locks[0]
        elif lock_index == 1:
            return self._locks[1]
        return self._locks[2]

    def set_lock(self, lock: Lock, lock_index: int):
        """
        Assigns a lock to a cave position.
        lock_index:
        0 = Lock 1
        1 = Lock 2
        2 = Lock 3 (default)
        """
        if lock_index == 0:
            self._locks[0] = lock
        elif lock_index == 1:
            self._locks[1] = lock
        else:
            self._locks[2] = lock

    def set_lethality(self, lethality: float, cave_index: int):
        """
        Sets lethality for a cave.
        cave_index:
        0 = Cave 1
        1 = Cave 2
        2 = Cave 3
        """
        self._lethality_levels[cave_index] = lethality

    def get_lethality(self, cave_index: int) -> float:
        """
        Returns lethality for a cave.
        cave_index:
        0 = Cave 1
        1 = Cave 2
        2 = Cave 3
        """
        return self._lethality_levels[cave_index]

    def cave_status(self, cave_index: int) -> str:
        """
        Displays cave information during gameplay.
        """
        return (
            f"--Cave: {self._locks[cave_index]._name}--\t"
            f"--Lethality: {self._lethality_levels[cave_index] * 100:.0f}%--\t"
            f"--Oxygen: {self._oxygen_levels[cave_index] * 100:.0f}%--\n"
        )

    def __str__(self) -> str:
        """
        Displays full cave information at the end of the game.
        """
        summary = ""
        for i in range(3):
            summary += (
                f"--Cave: {self._locks[i]._name}--\t"
                f"--Lethality: {self._lethality_levels[i]}--\t"
                f"--Oxygen: {self._oxygen_levels[i]}--\n\n"
            )
            for gem in self._locks[i]._gems:
                summary += f"{gem}\n"
            summary += "\n"
        return summary

cave = Cave()
print(cave.cave_status(0))
print(cave.cave_status(1))
print(cave.cave_status(2))
cave.decrease_cave_oxygen(0, 0.25)
cave.decrease_cave_oxygen(1, 0.35)
cave.decrease_cave_oxygen(2, 0.55)
print(cave.cave_status(0))
print(cave.cave_status(1))
print(cave.cave_status(2))
