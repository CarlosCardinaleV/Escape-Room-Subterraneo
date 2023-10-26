import Jugador

class Equipo:
    def __init__(self, nombre="Equipo #", nombre_jugador_a="fulano 1",
                 nombre_jugador_b="fulano 2", nombre_jugador_c="fulano 3"):
        """
        Inicializa una instancia de Equipo.

        Args:
            nombre (str): El nombre del equipo (por defecto, "Equipo #").
        """
        self.nombre_equipo = nombre
        self.nombres_jugadores = [nombre_jugador_a, nombre_jugador_b, nombre_jugador_c]
        #self.nombreJugadorA = nombreJugadorA
        #self.nombreJugadorB = nombreJugadorB
        #self.nombreJugadorC = nombreJugadorC
        self.jugador_del_equipo = []
        for i in range(3):
            self.jugador_del_equipo.append(Jugador.Jugador(self.nombres_jugadores[i]))
        self.equipo_vivo = True

    def get_nombre_equipo(self):
        """
        Obtiene el nombre del equipo.

        Returns:
            str: El nombre del equipo.
        """
        return self.nombre_equipo

    def get_jugador_del_equipo(self, cual_jugador):
        """
        Obtiene un jugador en el equipo por su número (1, 2 o 3).

        Args:
            cualJugador (int): El número del jugador deseado (1, 2 o 3).

        Returns:
            Jugador: El jugador seleccionado.
        """
        try:
            if cual_jugador+1 == 1:
                return self.jugadorEquipo[cual_jugador]
            elif cual_jugador+1 == 2:
                return self.jugadorEquipo[cual_jugador]
            elif cual_jugador+1 == 3:
                return self.jugadorEquipo[cual_jugador]
            else:
                print("Número de gema no válido. Debe ser 1, 2 o 3.")
                return None
        except IndexError:
            print("Índice de gema fuera de rango. El jugador no tiene esa gema.")
            return None

    def get_equipo_vivo(self):
        """
        Comprueba si el equipo está vivo.

        Returns:
            bool: True si el equipo está vivo, False de lo contrario.
        """
        return self.equipo_vivo

    def set_nombre_equipo(self, equipo):
        """
        Establece el nombre del equipo.

        Args:
            equipo (str): El nombre del equipo.

        Returns:
            None
        """
        self.nombre_equipo = equipo

    def set_jugador_equipo(self, jugador, cual_jugador):
        """
        Establece un jugador en el equipo por su número (1, 2 o 3).

        Args:
            jugador (Jugador): El jugador a establecer.
            cualJugador (int): El número del jugador en el equipo (1, 2 o 3).

        Returns:
            None
        """
        self.jugadorEquipo[cual_jugador - 1] = jugador

    def se_equipo_vivo(self, vivo):
        """
        Establece el estado de vida del equipo.

        Args:
            vivo (bool): True si el equipo está vivo, False de lo contrario.

        Returns:
            None
        """
        self.equipo_vivo = vivo

    def __str__(self):
        """
        Obtiene una representación de cadena del equipo, incluyendo información
        sobre su nombre, jugadores vivos y gemas.

        Returns:
            str: Una cadena que describe el equipo.
        """
        informacion = "\n" + "Nombre del equipo: " + self.nombre_equipo + "\n"
        cuantos_jugadores_vivos = sum(1 for jugador in self.jugador_del_equipo if jugador.get_vida_jugador())
        informacion += "Cuantos jugadores vivos: " + str(cuantos_jugadores_vivos) + "\n"
        informacion += "Jugadores:\n"
        #for i in range(3):
        #    informacion += self.jugadorDelEquipo[i].getNombreJugador() + "    \t"
        #informacion += "\n"
        for i in range(3):
            informacion += "\t" + self.jugador_del_equipo[i].get_nombre_jugador() + ":\n"
            for j in range(3):
                informacion += str(self.jugador_del_equipo[i].get_gema_jugador(j)) + "\n"
            informacion += "\n"
        return informacion
