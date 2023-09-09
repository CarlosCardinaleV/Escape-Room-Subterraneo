import Jugador

class Equipo:
    def __init__(self, nombre="Equipo #"):
        self.nombreEquipo = nombre
        self.jugadorEquipo = [Jugador() for _ in range(3)]
        self.vivoEquipo = True

    def getNombreEquipo(self):
        return self.nombreEquipo

    def getJugadorEquipo(self, cualJugador):
        if cualJugador == 1:
            return self.jugadorEquipo[0]
        elif cualJugador == 2:
            return self.jugadorEquipo[1]
        else:
            return self.jugadorEquipo[2]

    def getVivoEquipo(self):
        return self.vivoEquipo

    def setNombreEquipo(self, equipo):
        self.nombreEquipo = equipo

    def setJugadorEquipo(self, jugador, cualJugador):
        self.jugadorEquipo[cualJugador - 1] = jugador

    def setVivoEquipo(self, vivo):
        self.vivoEquipo = vivo

    def toStringEquipo(self):
        informacion = "Nombre del equipo: " + self.nombreEquipo + "   \t"
        cuantosJugadoresVivos = sum(1 for jugador in self.jugadorEquipo if jugador.getVidaJugador())
        informacion += "Cuantos Vivos:   " + str(cuantosJugadoresVivos) + " \n"
        informacion += "Jugadores:   \t" + self.getJugadorEquipo(1).getNombreJugador() + "    "
        informacion += self.getJugadorEquipo(2).getNombreJugador() + "    "
        informacion += self.getJugadorEquipo(3).getNombreJugador() + "  \n\n"
        for i in range(3):
            informacion += self.jugadorEquipo[i].toStringJugador()
        return informacion

    def __str__(self):
        informacion = "\n" + "Nombre del equipo: " + self.nombreEquipo + "\n"
        cuantosJugadoresVivos = sum(1 for jugador in self.jugadorEquipo if jugador.getVidaJugador())
        informacion += "Cuantos Vivos: " + str(cuantosJugadoresVivos) + "\n"
        informacion += "Jugadores:   \t"
        for i in range(3):
            informacion += self.jugadorEquipo[i].getNombreJugador() + "    \t"
        informacion += "\n"
        for i in range(3):
            for j in range(3):
                informacion += self.jugadorEquipo[i].getGemaJugador(j).toString() + "\n"
            informacion += "\n"
        return informacion

    def desplegarEquipo(self):
        print("Nombre del equipo: " + self.nombreEquipo)
        cuantosJugadoresVivos = sum(1 for jugador in self.jugadorEquipo if jugador.getVidaJugador())
        print("Cuantos Vivos: " + str(cuantosJugadoresVivos))
        print("Jugadores:\n")
        for i in range(3):
            print(self.jugadorEquipo[i].getNombreJugador() + " -->\t", end="")
            for j in range(3):
                print(self.jugadorEquipo[i].getGemaJugador(j).toStringGema() + "\t", end="")
            print("\n")
