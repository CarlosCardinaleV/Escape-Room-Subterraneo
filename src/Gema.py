import random

class Gema:
    """
    La clase Gema representa una gema con atributos como tipo, jugador,
    vida, ataque y defensa.
    """
    def __init__(self, tipo: str="no especificado", propietario: str = "player#", \
                 ataque: float = 0.0, defensa: float = 0.0, vida: float = 100.0):
        """
        Inicializa una nueva instancia de la clase Gema.
        Args:
            _tipo (str): El tipo de la gema.
            _jugador (str): El nombre del jugador propietario de la gema.
            _ataque (float): El valor de ataque de la gema.
            _defensa (float): El valor de defensa de la gema.
            _vida (float): El valor de vida de la gema.
        """
        self._tipo = tipo
        self._propietario = propietario
        self._vida = vida
        self._ataque = ataque
        self._defensa = defensa

    def __str__(self) -> str:
        """
        Devuelve una representación de cadena de la gema, incluyendo información sobre
        el jugador, vida, ataque, defensa y tipo de gema.
        Returns:
            str: Una cadena que describe la gema.
        """
        return f"\t Gema de: {self._propietario} \n \
        Vida: {self._vida}% \n \
        Ataque: {self._ataque} \n \
        Defensa: {self._defensa} \n \
        Tipo: {self._tipo}"

    def __str__gema(self) -> str:
        return f"{self._tipo}: {self._vida}%"

    @property
    def tipo(self) -> str:
        """
        Obtiene el tipo de la gema.
        Returns:
            str: El tipo de la gema.
        """
        return self._tipo

    @property
    def propietario(self) -> str:
        """
        Obtiene el nombre del jugador propietario de la gema.
        Returns:
            str: El nombre del jugador propietario de la gema.
        """
        return self._propietario

    @property
    def vida(self) -> float:
        """
        Obtiene el valor de vida de la gema.
        Returns:
            float: El valor de vida de la gema.
        """
        return self._vida

    @property
    def ataque(self) -> float:
        """
        Obtiene el valor de ataque de la gema.
        Returns:
            float: El valor de ataque de la gema.
        """
        return self._ataque

    @property
    def defensa(self) -> float:
        """
        Obtiene el valor de defensa de la gema.
        Returns:
            float: El valor de defensa de la gema.
        """
        return self._defensa

    @tipo.setter
    def tipo(self, nuevo_tipo: str) -> None:
        """
        Establece el tipo de la gema.
        Args:
            tipo (str): El tipo de la gema a establecer.
        """
        self._tipo = nuevo_tipo

    @propietario.setter
    def propietario(self, nuevo_propietario: str) -> None:
        """
        Establece el nombre del jugador propietario de la gema.

        Args:
            jugador (str): El nombre del jugador propietario de la gema.
        """
        self._propietario = nuevo_propietario

    @vida.setter
    def vida(self, nueva_vida: str) -> None:
        """
        Establece el valor de vida de la gema, asegurándose de que no sea un valor negativo.

        Args:
            vida (float): El valor de vida de la gema a establecer.
        """
        try:
            if nueva_vida >= 0 and nueva_vida <= 100:
                self._vida = nueva_vida
            else:
                self._vida = 0.0
        except ValueError:
            raise ValueError("El valor de vida tiene que ser un numero.")

    @ataque.setter
    def ataque(self, nuevo_ataque: float) -> None:
        """
        Establece el valor de ataque de la gema.

        Args:
            ataque (float): El valor de ataque de la gema a establecer.
        """
        self._ataque = nuevo_ataque

    @defensa.setter
    def defensa(self, nueva_defensa: float) -> None:
        """
        Establece el valor de defensa de la gema.

        Args:
            defensa (float): El valor de defensa de la gema a establecer.
        """
        self._defensa = nueva_defensa

