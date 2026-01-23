from dataclasses import dataclass, field
from typing import List, Optional

from Spell import Spell
from Player import Player
from Cave import Cave
from Team import Team


@dataclass
class ScapeRoomConsole:
    """
    ScapeRoomConsole manages the console-based execution
    of the Escape Room Subterraneo game.
    """

    _best_position: int = field(default=0)
    _spell: Optional[Spell] = field(default=None)
    _team: List[Team] = field(default_factory=list)
    _cave: List[Cave] = field(default_factory=list)
    _player: List[Player] = field(default_factory=list)
    _seconds_spell: float = field(default=0.0)

    def run(self):
        """
        Main method to run the application in console mode.
        """

        # Equivalent to InterfazConsola.solicitarInt(...)
        cuantos_equipos = int(
            input(
                "Cuantos Equipos participan en el torneo de "
                "SCAPE ROOM SUBTERRANEO? "
            )
        )

        # Initialize arrays (lists in Python)
        self._team = [None] * cuantos_equipos
        self._cave = [None] * cuantos_equipos

        # Example of initializing objects later
        for i in range(cuantos_equipos):
            self._team[i] = Team()
            self._cave[i] = Cave()

        print(f"\nSe han creado {cuantos_equipos} equipos y cavernas.")

ScapeRoomConsole().run()