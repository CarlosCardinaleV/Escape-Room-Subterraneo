import Gema

class Jugador:
    def __init__(self, name="Jugador #"):
        self.vidaJugador = True
        self.oxigenoJugador = 1.0
        tipo = ["FUEGO", "AGUA", "METAL"]
        self.nombreJugador = name
        self.gemaJugador = []
        for i in range(3):
            self.gemaJugador.append(Gema(name, tipo[i]))

    def getGemaJugador(self, cualGema):
        if cualGema == 1:
            return self.gemaJugador[0]
        elif cualGema == 2:
            return self.gemaJugador[1]
        else:
            return self.gemaJugador[2]

    def setVidaGemaJugador(self, cualGema, vida):
        if cualGema == 1:
            self.gemaJugador[0].setVidaGema(vida)
        elif cualGema == 2:
            self.gemaJugador[1].setVidaGema(vida)
        else:
            self.gemaJugador[2].setVidaGema(vida)

    def getNombreJugador(self):
        return self.nombreJugador

    def setNombreJugador(self, nombre):
        self.nombreJugador = nombre

    def setVidaJugador(self, vida):
        self.vidaJugador = vida

    def getVidaJugador(self):
        return self.vidaJugador

    def setOxigenoJugador(self, oxigeno):
        self.oxigenoJugador = oxigeno

    def getOxigenoJugador(self):
        return self.oxigenoJugador

    def __str__(self):
        informacion = ""
        informacion = "\n" + "Nombre del jugador: " + self.nombreJugador + "\n"
        informacion += "Oxigeno del jugador: " + str(self.oxigenoJugador) + "\n"
        informacion += "Sigue vivo? " + str(self.vidaJugador) + "\n"
        informacion += "Gemas: \n"
        for i in range(3):
            informacion += self.gemaJugador[i].__str__() + "\n"
        return informacion

    def toStringJugador(self):
        informacion = ""
        informacion = "\n\n" + "Nombre del jugador: " + self.nombreJugador + "\t"
        informacion += "Sigue vivo? " + str(self.vidaJugador) + "  \n"
        informacion += "Gemas: \t"
        for i in range(3):
            informacion += "  " + self.gemaJugador[i].toStringGema() + "  \t"
        return informacion

    def desplegarJugador(self):
        print("Nombre del Jugador: " + self.nombreJugador)
        print("Oxigeno del jugador: " + str(self.oxigenoJugador))
        print("Sigue vivo? " + str(self.vidaJugador))
        print("Gemas:")
        for i in range(3):
            print(self.gemaJugador[i].toString())
