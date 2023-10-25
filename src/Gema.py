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
        self.tipoGema = tipo
        self.jugadorGema = jugador
        self.vidaGema = vida
        self.ataqueGema = ataque
        self.defensaGema = defensa

    def __str__(self):
        """
        Devuelve una representación de cadena de la gema, incluyendo información sobre
        el jugador, vida, ataque, defensa y tipo de gema.

        Returns:
            str: Una cadena que describe la gema.
        """
        informacion = ""
        #informacion += "Gema de: " + self.jugadorGema + "\n"
        informacion += "\tVida de la Gema: " + str(self.vidaGema * 100.0) + "%\n"
        informacion += "\tAtaque: " + str(self.ataqueGema) + "%\n"
        informacion += "\tDefensa: " + str(self.defensaGema) + "%\n"
        informacion += "\tEl tipo de Gema: " + self.tipoGema + "\n"
        return informacion

    def __str__gema(self):
        return f"{self.tipoGema}:{self.vidaGema * 100.0}%"

    def desplegarGema(self):
        """
        Muestra información sobre la gema en la consola, incluyendo el jugador, vida,
        ataque, defensa y tipo de gema.
        """
        print("Gema de: " + self.jugadorGema)
        print("Vida de la Gema: " + str(self.vidaGema * 100.0) + "%")
        print("Ataque: " + str(self.ataqueGema))
        print("Defensa: " + str(self.defensaGema))
        print("El tipo de Gema: " + self.tipoGema)

    def getTipoGema(self):
        """
        Obtiene el tipo de la gema.

        Returns:
            str: El tipo de la gema.
        """
        return self.tipoGema

    def getPropietarioGema(self):
        """
        Obtiene el nombre del jugador propietario de la gema.

        Returns:
            str: El nombre del jugador propietario de la gema.
        """
        return self.jugadorGema

    def getVidaGema(self):
        """
        Obtiene el valor de vida de la gema.

        Returns:
            float: El valor de vida de la gema.
        """
        return self.vidaGema

    def getAtaqueGema(self):
        """
        Obtiene el valor de ataque de la gema.

        Returns:
            float: El valor de ataque de la gema.
        """
        return self.ataqueGema

    def getDefensaGema(self):
        """
        Obtiene el valor de defensa de la gema.

        Returns:
            float: El valor de defensa de la gema.
        """
        return self.defensaGema

    def setTipoGema(self, tipo):
        """
        Establece el tipo de la gema.

        Args:
            tipo (str): El tipo de la gema a establecer.
        """
        self.tipoGema = tipo

    def setJugadorGema(self, jugador):
        """
        Establece el nombre del jugador propietario de la gema.

        Args:
            jugador (str): El nombre del jugador propietario de la gema.
        """
        self.jugadorGema = jugador

    def setVidaGema(self, vida):
        """
        Establece el valor de vida de la gema, asegurándose de que no sea un valor negativo.

        Args:
            vida (float): El valor de vida de la gema a establecer.
        """
        if vida >= 0:
            self.vidaGema = vida
        else:
            self.vidaGema = 0.0

    def setAtaqueGema(self, ataque):
        """
        Establece el valor de ataque de la gema.

        Args:
            ataque (float): El valor de ataque de la gema a establecer.
        """
        self.ataqueGema = ataque

    def setDefensaGema(self, defensa):
        """
        Establece el valor de defensa de la gema.

        Args:
            defensa (float): El valor de defensa de la gema a establecer.
        """
        self.defensaGema = defensa
