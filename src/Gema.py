import random

class Gema:
    """
    La clase Gema representa una gema con atributos como tipo, jugador, vida, ataque y defensa.
    """
    def __init__(self, tipo="", jugador="", ataque=0.0, defensa=0.0):
        """
        Inicializa una nueva instancia de la clase Gema.

        Args:
            tipo (str): El tipo de la gema (por defecto, cadena vacía).
            jugador (str): El nombre del jugador propietario de la gema (por defecto, cadena vacía).
            ataque (float): El valor de ataque de la gema (por defecto, 0.0).
            defensa (float): El valor de defensa de la gema (por defecto, 0.0).
        """
        self.tipoGema = tipo
        self.jugadorGema = jugador
        self.vidaGema = 1.0
        self.ataqueGema = ataque
        self.defensaGema = defensa

    def __random_type(self):
        """
        Método privado que genera aleatoriamente un tipo de gema (FUEGO, AGUA, METAL).

        Returns:
            str: El tipo de gema generado aleatoriamente.
        """
        valor = random.randint(1, 3)
        if valor == 1:
            return "FUEGO"
        elif valor == 2:
            return "AGUA"
        else:
            return "METAL"

    def __random_value(self, min_val, max_val):
        """
        Método privado que genera un valor aleatorio en un rango específico.

        Args:
            min_val (float): El valor mínimo del rango.
            max_val (float): El valor máximo del rango.

        Returns:
            float: Un valor aleatorio dentro del rango especificado.
        """
        return min_val + random.random() * (max_val - min_val)

    def __str__(self):
        """
        Devuelve una representación de cadena de la gema, incluyendo información sobre el jugador, vida, ataque, defensa y tipo de gema.

        Returns:
            str: Una cadena que describe la gema.
        """
        informacion = ""
        informacion += "Gema de: " + self.jugadorGema + "\n"
        informacion += "Vida de la Gema: " + str(self.vidaGema * 100.0) + "%\n"
        informacion += "Ataque: " + str(self.ataqueGema) + "\n"
        informacion += "Defensa: " + str(self.defensaGema) + "\n"
        informacion += "El tipo de Gema: " + self.tipoGema + "\n"
        return informacion

    def __str__gema(self):
        return f"{self.tipoGema}:{self.vidaGema * 100.0}%"

    def desplegarGema(self):
        """
        Muestra información sobre la gema en la consola, incluyendo el jugador, vida, ataque, defensa y tipo de gema.
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

    @staticmethod
    def numRandom(min_val, max_val):
        """
        Método estático que genera un número aleatorio dentro de un rango especificado.

        Args:
            min_val (float): El valor mínimo del rango.
            max_val (float): El valor máximo del rango.

        Returns:
            float: Un número aleatorio dentro del rango especificado.
        """
        return min_val + random.random() * (max_val - min_val)