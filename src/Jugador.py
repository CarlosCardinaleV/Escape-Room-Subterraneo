import random
import Gema

class Jugador:
    """
    La clase Jugador representa a un jugador con atributos como su nombre,
    estado de vida, nivel de oxígeno y gemas.
    """
    def __init__(self, nombre="anonimo"):
        """
        Inicializa una nueva instancia de la clase Jugador.

        Args:
            nombre (str): El nombre del jugador (por defecto, "anonimo").
        """
        self.vidaJugador = True
        self.oxigenoJugador = 1.0 * 100
        tipo = ["FUEGO", "AGUA", "METAL"]
        self.nombreJugador = nombre
        self.gemaJugador = []
        for i in range(3):
            nueva_gema = Gema.Gema(jugador=self.nombreJugador, tipo=tipo[i],
                        ataque=round(random.uniform(0.6, 1.0) * 100, 2),
                        defensa=round(random.uniform(0.1, 0.5) * 100, 2))
            self.gemaJugador.append(nueva_gema)

    def getGemaJugador(self, cualGema):
        """
        Obtiene una de las gemas del jugador por su número (1, 2 o 3).

        Args:
            cualGema (int): El número de la gema deseada (1, 2 o 3).

        Returns:
            Gema: La gema seleccionada, o None si el número de gema no es válido.
        """
        try:
            if cualGema == 1:
                return self.gemaJugador[cualGema-1]
            elif cualGema == 2:
                return self.gemaJugador[cualGema-1]
            elif cualGema == 3:
                return self.gemaJugador[cualGema-1]
            else:
                # Handle the case when cualGema is not 1, 2, or 3
                print("Número de gema no válido. Debe ser 1, 2 o 3.")
                return None
        except IndexError:
            # Handle the case when the list index is out of range
            print("Índice de gema fuera de rango. El jugador no tiene esa gema.")
            return None


    def setVidaGemaJugador(self, cualGema, vida):
        """
        Establece el valor de vida de una de las gemas del jugador por su número (1, 2 o 3).

        Args:
            cualGema (int): El número de la gema a la que se le cambiará la vida (1, 2 o 3).
            vida (float): El nuevo valor de vida de la gema.
        """
        try:
            if cualGema == 1:
                self.gemaJugador[cualGema-1].setVidaGema(vida)
            elif cualGema == 2:
                self.gemaJugador[cualGema-1].setVidaGema(vida)
            elif cualGema == 3:
                self.gemaJugador[cualGema-1].setVidaGema(vida)
            else:
                print("Número de gema no válido. Debe ser 1, 2 o 3.")
                return None
        except IndexError:
            print("Índice de gema fuera de rango. El jugador no tiene esa gema.")
            return None

    def getNombreJugador(self):
        """
        Obtiene el nombre del jugador.

        Returns:
            str: El nombre del jugador.
        """
        return self.nombreJugador

    def setNombreJugador(self, nombre):
        """
        Establece el nombre del jugador.

        Args:
            nombre (str): El nuevo nombre del jugador.
        """
        self.nombreJugador = nombre

    def setVidaJugador(self, vida):
        """
        Establece el estado de vida del jugador.

        Args:
            vida (bool): El estado de vida del jugador (True para vivo, False para no vivo).
        """
        self.vidaJugador = vida

    def getVidaJugador(self):
        """
        Obtiene el estado de vida del jugador.

        Returns:
            bool: True si el jugador está vivo, False si no lo está.
        """
        return self.vidaJugador

    def setOxigenoJugador(self, oxigeno):
        """
        Establece el nivel de oxígeno del jugador.

        Args:
            oxigeno (float): El nuevo nivel de oxígeno del jugador.
        """
        self.oxigenoJugador = oxigeno

    def getOxigenoJugador(self):
        """
        Obtiene el nivel de oxígeno del jugador.

        Returns:
            float: El nivel de oxígeno del jugador.
        """
        return self.oxigenoJugador

    def __str__(self):
        """
        Devuelve una representación de cadena del jugador, incluyendo
        información sobre su nombre, oxígeno, estado de vida y gemas.

        Returns:
            str: Una cadena que describe el jugador y sus gemas.
        """
        informacion = ""
        informacion = "\n" + "Nombre del jugador: " + self.nombreJugador + "\n"
        informacion += "Oxigeno del jugador: " + str(self.oxigenoJugador) + "%\n"
        informacion += "Sigue vivo? " + ("Sí" if self.vidaJugador else "No") + "\n"
        informacion += "Gemas: \n"
        for i in range(3):
            informacion += self.gemaJugador[i].__str__() + "\n"
        return informacion

    def desplegarJugador(self):
        """
        Muestra información sobre el jugador en la consola, incluyendo el
        nombre, oxígeno, estado de vida y gemas.
        """
        print("Nombre del Jugador: " + self.nombreJugador)
        print("Oxigeno del jugador: " + str(self.oxigenoJugador))
        print("Sigue vivo? " + str(self.vidaJugador))
        print("Gemas:")
        for i in range(3):
            print(self.gemaJugador[i].toString())
