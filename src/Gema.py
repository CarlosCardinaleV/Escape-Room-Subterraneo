import random

class Gema:
    """
    La clase Gema representa una gema con atributos como tipo, jugador,
    vida, ataque y defensa.
    """
    def __init__(self, tipo="no especificado", jugador="anonimo", ataque=0.0, defensa=0.0, vida=1.0):
        """
        Inicializa una nueva instancia de la clase Gema.

        Args:
            tipo (str): El tipo de la gema.
            jugador (str): El nombre del jugador propietario de la gema.
            ataque (float): El valor de ataque de la gema.
            defensa (float): El valor de defensa de la gema.
            vida (float): El valor de vida de la gema.
        """
        self.__tipo_gema = tipo
        self.__jugador_gema = jugador
        self.__vida_gema = vida
        self.__ataque_gema = ataque
        self.__defensa_gema = defensa

    def __str__(self):
        """
        Devuelve una representación de cadena de la gema, incluyendo información sobre
        el jugador, vida, ataque, defensa y tipo de gema.

        Returns:
            str: Una cadena que describe la gema.
        """
        informacion = ""
        informacion += "\tGema de: " + self.__jugador_gema + "\n"
        informacion += "\tVida de la Gema: " + str(self.__vida_gema * 100.0) + "%\n"
        informacion += "\tAtaque: " + str(self.__ataque_gema) + "%\n"
        informacion += "\tDefensa: " + str(self.__defensa_gema) + "%\n"
        informacion += "\tEl tipo de Gema: " + self.__tipo_gema + "\n"
        return informacion

    def __str__gema(self):
        return f"{self.__tipo_gema}:{self.__vida_gema * 100.0}%"

    def get_tipo_gema(self):
        """
        Obtiene el tipo de la gema.

        Returns:
            str: El tipo de la gema.
        """
        return self.__tipo_gema

    def get_propietario_gema(self):
        """
        Obtiene el nombre del jugador propietario de la gema.

        Returns:
            str: El nombre del jugador propietario de la gema.
        """
        return self.__jugador_gema

    def get_vida_gema(self):
        """
        Obtiene el valor de vida de la gema.

        Returns:
            float: El valor de vida de la gema.
        """
        return self.__vida_gema

    def get_ataque_gema(self):
        """
        Obtiene el valor de ataque de la gema.

        Returns:
            float: El valor de ataque de la gema.
        """
        return self.__ataque_gema

    def get_defensa_gema(self):
        """
        Obtiene el valor de defensa de la gema.

        Returns:
            float: El valor de defensa de la gema.
        """
        return self.__defensa_gema

    def set_tipo_gema(self, tipo):
        """
        Establece el tipo de la gema.

        Args:
            tipo (str): El tipo de la gema a establecer.
        """
        self.__tipo_gema = tipo

    def set_jugador_gema(self, jugador):
        """
        Establece el nombre del jugador propietario de la gema.

        Args:
            jugador (str): El nombre del jugador propietario de la gema.
        """
        self.__jugador_gema = jugador

    def set_vida_gema(self, vida):
        """
        Establece el valor de vida de la gema, asegurándose de que no sea un valor negativo.

        Args:
            vida (float): El valor de vida de la gema a establecer.
        """
        if vida >= 0:
            self.__vida_gema = vida
        else:
            self.__vida_gema = 0.0

    def set_ataque_gema(self, ataque):
        """
        Establece el valor de ataque de la gema.

        Args:
            ataque (float): El valor de ataque de la gema a establecer.
        """
        self.__ataque_gema = ataque

    def set_defensa_gema(self, defensa):
        """
        Establece el valor de defensa de la gema.

        Args:
            defensa (float): El valor de defensa de la gema a establecer.
        """
        self.__defensa_gema = defensa
