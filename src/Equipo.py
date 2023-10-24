import Jugador

class Equipo:
    def __init__(self, nombre="Equipo #"):
        """
        Inicializa una instancia de Equipo.

        Args:
            nombre (str): El nombre del equipo (por defecto, "Equipo #").
        """
        self.nombreEquipo = nombre
        self.jugadorEquipo = [Jugador() for _ in range(3)]
        self.vivoEquipo = True

    def getNombreEquipo(self):
        """
        Obtiene el nombre del equipo.

        Returns:
            str: El nombre del equipo.
        """
        return self.nombreEquipo

    def getJugadorEquipo(self, cualJugador):
        """
        Obtiene un jugador en el equipo por su número (1, 2 o 3).

        Args:
            cualJugador (int): El número del jugador deseado (1, 2 o 3).

        Returns:
            Jugador: El jugador seleccionado.
        """
        if cualJugador == 1:
            return self.jugadorEquipo[0]
        elif cualJugador == 2:
            return self.jugadorEquipo[1]
        else:
            return self.jugadorEquipo[2]

    def getVivoEquipo(self):
        """
        Comprueba si el equipo está vivo.

        Returns:
            bool: True si el equipo está vivo, False de lo contrario.
        """
        return self.vivoEquipo

    def setNombreEquipo(self, equipo):
        """
        Establece el nombre del equipo.

        Args:
            equipo (str): El nombre del equipo.

        Returns:
            None
        """
        self.nombreEquipo = equipo

    def setJugadorEquipo(self, jugador, cualJugador):
        """
        Establece un jugador en el equipo por su número (1, 2 o 3).

        Args:
            jugador (Jugador): El jugador a establecer.
            cualJugador (int): El número del jugador en el equipo (1, 2 o 3).

        Returns:
            None
        """
        self.jugadorEquipo[cualJugador - 1] = jugador

    def setVivoEquipo(self, vivo):
        """
        Establece el estado de vida del equipo.

        Args:
            vivo (bool): True si el equipo está vivo, False de lo contrario.

        Returns:
            None
        """
        self.vivoEquipo = vivo

    def toStringEquipo(self):
        """
        Obtiene una representación de cadena del equipo, incluyendo información
        sobre su nombre, jugadores vivos y gemas.

        Returns:
            str: Una cadena que describe el equipo.
        """
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
        """
        Obtiene una representación de cadena del equipo, incluyendo información
        sobre su nombre, jugadores vivos y gemas.

        Returns:
            str: Una cadena que describe el equipo.
        """
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
        """
        Imprime información sobre el equipo, incluyendo el nombre del equipo,
        jugadores vivos y gemas.

        Returns:
            None
        """
        print("Nombre del equipo: " + self.nombreEquipo)
        cuantosJugadoresVivos = sum(1 for jugador in self.jugadorEquipo if jugador.getVidaJugador())
        print("Cuantos Vivos: " + str(cuantosJugadoresVivos))
        print("Jugadores:\n")
        for i in range(3):
            print(self.jugadorEquipo[i].getNombreJugador() + " -->\t", end="")
            for j in range(3):
                print(self.jugadorEquipo[i].getGemaJugador(j).toStringGema() + "\t", end="")
            print("\n")
