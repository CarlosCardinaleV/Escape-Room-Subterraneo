import Jugador
import Cerrojo

class Hechizo:
    def __init__(self, segundos=1.0, contador=0):
        self.segundosHechizo = segundos
        self.contadorHechizo = contador

    def setContadorHechizo(self, contador):
        self.contadorHechizo += contador

    def getContadorHechizo(self):
        return self.contadorHechizo

    def setSegundosHechizo(self, segundos):
        if segundos >= 1.0:
            self.segundosHechizo = segundos
        else:
            self.segundosHechizo = 1.0

    def getSegundosHechizo(self):
        return self.segundosHechizo

    def vidaEnfrentamientoJugadorCerrojo(self, jugador, cerrojo, cualGemaJugador, cualGemaCerrojo):
        vidaGemaJugador = jugador.getGemaJugador(cualGemaJugador).getVidaGema()
        vidaGemaCerrojo = cerrojo.getGemaCerrojo(cualGemaCerrojo).getVidaGema()
        ataqueGemaJugador = jugador.getGemaJugador(cualGemaJugador).getAtaqueGema()
        ataqueGemaCerrojo = cerrojo.getGemaCerrojo(cualGemaCerrojo).getAtaqueGema()
        defensaGemaJugador = jugador.getGemaJugador(cualGemaJugador).getDefensaGema()
        defensaGemaCerrojo = cerrojo.getGemaCerrojo(cualGemaCerrojo).getDefensaGema()
        tipoGemaJugador = jugador.getGemaJugador(cualGemaJugador).getTipoGema()
        tipoGemaCerrojo = cerrojo.getGemaCerrojo(cualGemaCerrojo).getTipoGema()

        if tipoGemaJugador == tipoGemaCerrojo:
            vidaGemaJugador -= (ataqueGemaCerrojo - defensaGemaJugador) * self.segundosHechizo
            vidaGemaCerrojo -= (ataqueGemaJugador - defensaGemaCerrojo) * self.segundosHechizo
            cerrojo.setVidaGemaCerrojo(cualGemaCerrojo, vidaGemaCerrojo)
            jugador.setVidaGemaJugador(cualGemaJugador, vidaGemaJugador)
        elif tipoGemaJugador == "FUEGO" and tipoGemaCerrojo == "METAL":
            vidaGemaCerrojo -= (ataqueGemaJugador - defensaGemaCerrojo) * self.segundosHechizo
            cerrojo.setVidaGemaCerrojo(cualGemaCerrojo, vidaGemaCerrojo)
        elif tipoGemaJugador == "METAL" and tipoGemaCerrojo == "FUEGO":
            vidaGemaJugador -= (ataqueGemaCerrojo - defensaGemaJugador) * self.segundosHechizo
            jugador.setVidaGemaJugador(cualGemaJugador, vidaGemaJugador)
        elif tipoGemaJugador == "AGUA" and tipoGemaCerrojo == "METAL":
            vidaGemaJugador -= (ataqueGemaCerrojo - defensaGemaJugador) * self.segundosHechizo
            jugador.setVidaGemaJugador(cualGemaJugador, vidaGemaJugador)
        elif tipoGemaJugador == "METAL" and tipoGemaCerrojo == "AGUA":
            vidaGemaCerrojo -= (ataqueGemaJugador - defensaGemaCerrojo) * self.segundosHechizo
            cerrojo.setVidaGemaCerrojo(cualGemaCerrojo, vidaGemaCerrojo)
        elif tipoGemaJugador == "FUEGO" and tipoGemaCerrojo == "AGUA":
            vidaGemaJugador -= (ataqueGemaCerrojo - defensaGemaJugador) * self.segundosHechizo
            jugador.setVidaGemaJugador(cualGemaJugador, vidaGemaJugador)
        elif tipoGemaJugador == "AGUA" and tipoGemaCerrojo == "FUEGO":
            vidaGemaCerrojo -= (ataqueGemaJugador - defensaGemaCerrojo) * self.segundosHechizo
            cerrojo.setVidaGemaCerrojo(cualGemaCerrojo, vidaGemaCerrojo)
        else:
            print("Hubo un error :(")
