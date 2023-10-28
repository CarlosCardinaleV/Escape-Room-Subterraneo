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

    def vida_enfrentamiento_jugador_cerrojo(self, jugador, cerrojo, cualGemaJugador, cualGemaCerrojo):
        """
        Realiza un enfrentamiento entre un jugador y un cerrojo usando un hechizo. Calcula los
        cambios en la vida de las gemas
        involucradas en el enfrentamiento.

        Args:
            jugador (Jugador): El jugador que realiza el hechizo.
            cerrojo (Cerrojo): El cerrojo objetivo del hechizo.
            cualGemaJugador (int): El número de la gema del jugador involucrada en el
            enfrentamiento (1, 2 o 3).
            cualGemaCerrojo (int): El número de la gema del cerrojo involucrada en el
            enfrentamiento (1, 2 o 3).

        Returns:
            None
        """
        vidaGemaJugador = jugador.getGemaJugador(cualGemaJugador).getVidaGema()
        vidaGemaCerrojo = cerrojo.getGemaCerrojo(cualGemaCerrojo).getVidaGema()
        ataqueGemaJugador = jugador.getGemaJugador(cualGemaJugador).getAtaqueGema()
        ataqueGemaCerrojo = cerrojo.getGemaCerrojo(cualGemaCerrojo).getAtaqueGema()
        defensaGemaJugador = jugador.getGemaJugador(cualGemaJugador).getDefensaGema()
        defensaGemaCerrojo = cerrojo.getGemaCerrojo(cualGemaCerrojo).getDefensaGema()
        tipoGemaJugador = jugador.getGemaJugador(cualGemaJugador).getTipoGema()
        tipoGemaCerrojo = cerrojo.getGemaCerrojo(cualGemaCerrojo).getTipoGema()

        if tipoGemaJugador == tipoGemaCerrojo:
            vidaGemaJugador -= (ataqueGemaCerrojo - defensaGemaJugador) * self.segundos_hechizo
            vidaGemaCerrojo -= (ataqueGemaJugador - defensaGemaCerrojo) * self.segundos_hechizo
            cerrojo.setVidaGemaCerrojo(cualGemaCerrojo, vidaGemaCerrojo)
            jugador.setVidaGemaJugador(cualGemaJugador, vidaGemaJugador)
        elif tipoGemaJugador == "FUEGO" and tipoGemaCerrojo == "METAL":
            vidaGemaCerrojo -= (ataqueGemaJugador - defensaGemaCerrojo) * self.segundos_hechizo
            cerrojo.setVidaGemaCerrojo(cualGemaCerrojo, vidaGemaCerrojo)
        elif tipoGemaJugador == "METAL" and tipoGemaCerrojo == "FUEGO":
            vidaGemaJugador -= (ataqueGemaCerrojo - defensaGemaJugador) * self.segundos_hechizo
            jugador.setVidaGemaJugador(cualGemaJugador, vidaGemaJugador)
        elif tipoGemaJugador == "AGUA" and tipoGemaCerrojo == "METAL":
            vidaGemaJugador -= (ataqueGemaCerrojo - defensaGemaJugador) * self.segundos_hechizo
            jugador.setVidaGemaJugador(cualGemaJugador, vidaGemaJugador)
        elif tipoGemaJugador == "METAL" and tipoGemaCerrojo == "AGUA":
            vidaGemaCerrojo -= (ataqueGemaJugador - defensaGemaCerrojo) * self.segundos_hechizo
            cerrojo.setVidaGemaCerrojo(cualGemaCerrojo, vidaGemaCerrojo)
        elif tipoGemaJugador == "FUEGO" and tipoGemaCerrojo == "AGUA":
            vidaGemaJugador -= (ataqueGemaCerrojo - defensaGemaJugador) * self.segundos_hechizo
            jugador.setVidaGemaJugador(cualGemaJugador, vidaGemaJugador)
        elif tipoGemaJugador == "AGUA" and tipoGemaCerrojo == "FUEGO":
            vidaGemaCerrojo -= (ataqueGemaJugador - defensaGemaCerrojo) * self.segundos_hechizo
            cerrojo.setVidaGemaCerrojo(cualGemaCerrojo, vidaGemaCerrojo)
        else:
            print("Hubo un error :(")
