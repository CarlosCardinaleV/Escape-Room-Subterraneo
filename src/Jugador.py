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
        TIPO = ["AGUA", "FUEGO", "METAL"]
        self.__vida_jugador = True
        self.__oxigeno_jugador = 1.0 * 100
        self.__nombre_jugador = nombre
        self.__gema_jugador = []
        for i in range(3):
            nueva_gema = Gema.Gema(propietario=self.__nombre_jugador, tipo=TIPO[i],
                        ataque=round(random.uniform(0.6, 1.0) * 100, 2),
                        defensa=round(random.uniform(0.1, 0.5) * 100, 2))
            self.__gema_jugador.append(nueva_gema)

    def get_gema_jugador(self, cual_gema):
        """
        Obtiene una de las gemas del jugador por su número (1, 2 o 3).

        Args:
            cualGema (int): El número de la gema deseada (1, 2 o 3).

        Returns:
            Gema: La gema seleccionada, o None si el número de gema no es válido.
        """
        try:
            if cual_gema-1 == 0:
                return self.__gema_jugador[0]
            elif cual_gema-1 == 1:
                return self.__gema_jugador[1]
            elif cual_gema-1 == 2:
                return self.__gema_jugador[2]
            else:
                # Handle the case when cualGema is not 1, 2, or 3
                print("Número de gema no válido. Debe ser 1, 2 o 3.")
                return None
        except IndexError:
            # para el caso que el indice esta fuera de rango
            print("Índice de gema fuera de rango. El jugador no tiene esa gema.")
            return None

    @property
    def nombre_jugador(self):
        """
        Obtiene el nombre del jugador.

        Returns:
            str: El nombre del jugador.
        """
        return self.__nombre_jugador

    @nombre_jugador.setter
    def nombre_jugador(self, nombre):
        """
        Establece el nombre del jugador.

        Args:
            nombre (str): El nuevo nombre del jugador.
        """
        self.__nombre_jugador = nombre

    @property
    def vida_jugador(self):
        """
        Obtiene el estado de vida del jugador.

        Returns:
            bool: True si el jugador está vivo, False si no lo está.
        """
        return self.__vida_jugador

    @vida_jugador.setter
    def vida_jugador(self, vida):
        """
        Establece el estado de vida del jugador.

        Args:
            vida (bool): El estado de vida del jugador (True para vivo, False para no vivo).
        """
        self.__vida_jugador = vida

    @property
    def oxigeno_jugador(self):
        """
        Obtiene el nivel de oxígeno del jugador.

        Returns:
            float: El nivel de oxígeno del jugador.
        """
        return self.__oxigeno_jugador
    
    @oxigeno_jugador.setter
    def oxigeno_jugador(self, oxigeno):
        """
        Establece el nivel de oxígeno del jugador.

        Args:
            oxigeno (float): El nuevo nivel de oxígeno del jugador.
        """
        self.__oxigeno_jugador = oxigeno

    def __str__(self):
        """
        Devuelve una representación de cadena del jugador, incluyendo
        información sobre su nombre, oxígeno, estado de vida y gemas.

        Returns:
            str: Una cadena que describe el jugador y sus gemas.
        """
        informacion = ""
        informacion = "\n" + "Nombre del jugador: " + self.__nombre_jugador + "\n"
        informacion += "Oxigeno del jugador: " + str(self.__oxigeno_jugador) + "%\n"
        informacion += "Sigue vivo? " + ("Sí" if self.__vida_jugador else "No") + "\n"
        informacion += "Gemas: \n"
        for i in range(3):
            informacion += self.__gema_jugador[i].__str__() + "\n"
        return informacion
