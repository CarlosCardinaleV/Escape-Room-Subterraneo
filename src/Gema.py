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
            tipo (str): El tipo de la gema (por defecto, "no especificado").
            jugador (str): El nombre del jugador propietario de la gema
                (por defecto, "anonimo").
            ataque (float): El valor de ataque de la gema (por defecto, 0.0).
            defensa (float): El valor de defensa de la gema (por defecto, 0.0).
            vida (float): El valor de vida de la gema (por defecto, 1.0).
        """
        self.tipo_gema = tipo
        self.jugador_gema = jugador
        self.vida_gema = vida
        self.ataque_gema = ataque
        self.defensa_gema = defensa

    def __str__(self):
        """
        Devuelve una representación de cadena de la gema, incluyendo información sobre
        el jugador, vida, ataque, defensa y tipo de gema.

        Returns:
            str: Una cadena que describe la gema.
        """
        informacion = ""
        informacion += "\tGema de: " + self.jugador_gema + "\n"
        informacion += "\tVida de la Gema: " + str(self.vida_gema * 100.0) + "%\n"
        informacion += "\tAtaque: " + str(self.ataque_gema) + "%\n"
        informacion += "\tDefensa: " + str(self.defensa_gema) + "%\n"
        informacion += "\tEl tipo de Gema: " + self.tipo_gema + "\n"
        return informacion

    def __str__gema(self):
        return f"{self.tipo_gema}:{self.vida_gema * 100.0}%"

    def get_tipo_gema(self):
        """
        Obtiene el tipo de la gema.

        Returns:
            str: El tipo de la gema.
        """
        return self.tipo_gema

    def get_propietario_gema(self):
        """
        Obtiene el nombre del jugador propietario de la gema.

        Returns:
            str: El nombre del jugador propietario de la gema.
        """
        return self.jugador_gema

    def get_vida_gema(self):
        """
        Obtiene el valor de vida de la gema.

        Returns:
            float: El valor de vida de la gema.
        """
        return self.vida_gema

    def get_ataque_gema(self):
        """
        Obtiene el valor de ataque de la gema.

        Returns:
            float: El valor de ataque de la gema.
        """
        return self.ataque_gema

    def get_defensa_gema(self):
        """
        Obtiene el valor de defensa de la gema.

        Returns:
            float: El valor de defensa de la gema.
        """
        return self.defensa_gema

    def set_tipo_gema(self, tipo):
        """
        Establece el tipo de la gema.

        Args:
            tipo (str): El tipo de la gema a establecer.
        """
        self.tipo_gema = tipo

    def set_jugador_gema(self, jugador):
        """
        Establece el nombre del jugador propietario de la gema.

        Args:
            jugador (str): El nombre del jugador propietario de la gema.
        """
        self.jugador_gema = jugador

    def set_vida_gema(self, vida):
        """
        Establece el valor de vida de la gema, asegurándose de que no sea un valor negativo.

        Args:
            vida (float): El valor de vida de la gema a establecer.
        """
        if vida >= 0:
            self.vida_gema = vida
        else:
            self.vida_gema = 0.0

    def set_ataque_gema(self, ataque):
        """
        Establece el valor de ataque de la gema.

        Args:
            ataque (float): El valor de ataque de la gema a establecer.
        """
        self.ataque_gema = ataque

    def set_defensa_gema(self, defensa):
        """
        Establece el valor de defensa de la gema.

        Args:
            defensa (float): El valor de defensa de la gema a establecer.
        """
        self.defensa_gema = defensa
