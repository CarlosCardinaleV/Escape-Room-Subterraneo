import Jugador
import Cerrojo

class Hechizo:
    def __init__(self, segundos=1.0, contador=0):
        """
        Inicializa una instancia de Hechizo.

        Args:
            segundos (float): La duración en segundos del hechizo
            (por defecto, 1.0).
            contador (int): El contador del hechizo (por defecto, 0).
        """
        self.segundos_hechizo = segundos
        self.contador_hechizo = contador

    def set_contador_hechizo(self, contador):
        """
        Establece el contador del hechizo.

        Args:
            contador (int): El valor del contador a establecer.

        Returns:
            None
        """
        self.contador_hechizo += contador

    def get_contador_hechizo(self):
        """
        Obtiene el valor del contador del hechizo.

        Returns:
            int: El valor del contador del hechizo.
        """
        return self.contador_hechizo

    def set_segundos_hechizo(self, segundos):
        """
        Establece la duración del hechizo en segundos.

        Args:
            segundos (float): La duración del hechizo en segundos
            (debe ser igual o mayor a 1.0).

        Returns:
            None
        """
        if segundos >= 1.0:
            self.segundos_hechizo = segundos
        else:
            self.segundos_hechizo = 1.0

    def get_segundos_hechizo(self):
        """
        Obtiene la duración en segundos del hechizo.

        Returns:
            float: La duración en segundos del hechizo.
        """
        return self.segundos_hechizo

    def vida_enfrentamiento_jugador_cerrojo(self, jugador, cerrojo, cual_gema_jugador, cual_gema_cerrojo):
        """
        Realiza un enfrentamiento entre un jugador y un cerrojo usando un hechizo. Calcula los
        cambios en la vida de las gemas
        involucradas en el enfrentamiento.

        Args:
            jugador (Jugador): El jugador que realiza el hechizo.
            cerrojo (Cerrojo): El cerrojo objetivo del hechizo.
            cual_gema_jugador (int): El número de la gema del jugador involucrada en el
            enfrentamiento (1, 2 o 3).
            cual_gema_cerrojo (int): El número de la gema del cerrojo involucrada en el
            enfrentamiento (1, 2 o 3).

        Returns:
            None
        """
        vida_gema_jugador = jugador.get_gema_jugador(cual_gema_jugador).get_vida_gema()
        vida_gema_cerrojo = cerrojo.get_gema_cerrojo(cual_gema_cerrojo).get_vida_gema()
        ataque_gema_jugador = jugador.get_gema_jugador(cual_gema_jugador).get_ataque_gema()
        ataque_gema_cerrojo = cerrojo.get_gema_cerrojo(cual_gema_cerrojo).get_ataque_gema()
        defensa_gema_jugador = jugador.get_gema_jugador(cual_gema_jugador).get_defensa_gema()
        defensa_gema_cerrojo = cerrojo.get_gema_cerrojo(cual_gema_cerrojo).get_defensa_gema()
        tipo_gema_jugador = jugador.get_gema_jugador(cual_gema_jugador).get_tipo_gema()
        tipo_gema_cerrojo = cerrojo.get_gema_cerrojo(cual_gema_cerrojo).get_tipo_gema()

        if tipo_gema_jugador == tipo_gema_cerrojo:
            vida_gema_jugador -= (ataque_gema_cerrojo - defensa_gema_jugador) * self.segundos_hechizo
            vida_gema_cerrojo -= (ataque_gema_jugador - defensa_gema_cerrojo) * self.segundos_hechizo
            cerrojo.set_vida_gema_cerrojo(cual_gema_cerrojo, vida_gema_cerrojo)
            jugador.set_vida_gema_jugador(cual_gema_jugador, vida_gema_jugador)
        elif tipo_gema_jugador == "FUEGO" and tipo_gema_cerrojo == "METAL":
            vida_gema_cerrojo -= (ataque_gema_jugador - defensa_gema_cerrojo) * self.segundos_hechizo
            cerrojo.set_vida_gema_cerrojo(cual_gema_cerrojo, vida_gema_cerrojo)
        elif tipo_gema_jugador == "METAL" and tipo_gema_cerrojo == "FUEGO":
            vida_gema_jugador -= (ataque_gema_cerrojo - defensa_gema_jugador) * self.segundos_hechizo
            jugador.set_vida_gema_jugador(cual_gema_jugador, vida_gema_jugador)
        elif tipo_gema_jugador == "AGUA" and tipo_gema_cerrojo == "METAL":
            vida_gema_jugador -= (ataque_gema_cerrojo - defensa_gema_jugador) * self.segundos_hechizo
            jugador.set_vida_gema_jugador(cual_gema_jugador, vida_gema_jugador)
        elif tipo_gema_jugador == "METAL" and tipo_gema_cerrojo == "AGUA":
            vida_gema_cerrojo -= (ataque_gema_jugador - defensa_gema_cerrojo) * self.segundos_hechizo
            cerrojo.set_vida_gema_cerrojo(cual_gema_cerrojo, vida_gema_cerrojo)
        elif tipo_gema_jugador == "FUEGO" and tipo_gema_cerrojo == "AGUA":
            vida_gema_jugador -= (ataque_gema_cerrojo - defensa_gema_jugador) * self.segundos_hechizo
            jugador.set_vida_gema_jugador(cual_gema_jugador, vida_gema_jugador)
        elif tipo_gema_jugador == "AGUA" and tipo_gema_cerrojo == "FUEGO":
            vida_gema_cerrojo -= (ataque_gema_jugador - defensa_gema_cerrojo) * self.segundos_hechizo
            cerrojo.set_vida_gema_cerrojo(cual_gema_cerrojo, vida_gema_cerrojo)
        else:
            print("Hubo un error :(")
