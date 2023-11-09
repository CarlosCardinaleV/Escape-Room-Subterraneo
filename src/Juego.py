import Caverna
import Equipo
import Hechizo

class Juego:
    def __init__(self):
        self.equipo = []
        self.caverna = []
        self.jugador = []
        self.hechizo = None
        self.mejor_posicion = 0
        self.segundos_hechizo = 0

    def correr(self):
        cantidad_equipos = int(input("Cuantos Equipos participan en el torneo de SCAPE ROOM SUBTERRANEO? "))

        for i in range(cantidad_equipos):
            gemas_muertas_jugador1 = 0
            gemas_muertas_jugador2 = 0
            gemas_muertas_jugador3 = 0
            contador_jugadores_muertos = 0
            no_hay_un_muerto = True
            no_hay_dos_muertos = True
            
            nombre_equipo = input("Escriba el nombre del equipo: ")
            nombre_jugador1 = input("Escriba el nombre del primer jugador: ")
            nombre_jugador2 = input("Escriba el nombre del segundo jugador: ")
            nombre_jugador3 = input("Escriba el nombre del tercer jugador: ")

            self.equipo.append(Equipo.Equipo(nombre=nombre_equipo, nombre_jugador_a=nombre_jugador1,
                            nombre_jugador_b=nombre_jugador2, nombre_jugador_c=nombre_jugador3))
            
            hechizo = Hechizo.Hechizo()
            self.caverna.append(Caverna.Caverna())
            eleccion_menu = self.menu_inicial(hechizo, self.caverna[i], self.equipo[i], self.mejor_posicion)

            self.destruir_cerrojo()
            
            if eleccion_menu == 2:
                 print("\n\nGAME OVER!\n\n" )

        return None
    
    def menu_inicial(self, hechizo, caverna, equipo, mejor_posicion):
        """
        Elige la acción que el equipo quiere realizar antes de entrar a una caverna.

        Args:
            caverna: La caverna a la que se va a entrar.
            equipo: El equipo que está jugando.
            mejor_posicion: La posición del equipo que más lejos ha llegado.
            hechizo: el objeto hechizo

        Returns:
            El número de la acción elegida por el usuario.
        """

        # Pide al usuario que elija una acción.
        eleccion = int(input(
            "Resumen del juego: \n" +
            caverna.__str__() + "\n" +
            "Numero de hechizos realizados: " + str(hechizo.get_contador_hechizo()) + "\n" +
            equipo.__str__() + "\n\n\n" +
            "1. Hacer un hechizo\n2. Abandonar el Juego\n3. Historial del juego\n"))

        # Si el usuario elige la opción 3, muestra el equipo que haya llegado más lejos.
        if mejor_posicion != 0 and eleccion == 3:
            eleccion = int(input(
                "El nombre del mejor equipo por el momento es: \n\n" +
                equipo[mejor_posicion].nombre_equipo +
                "\n\n\n1.Seguir jugando\n2. Abandonar el juego"))
        
        elif mejor_posicion == 0 and eleccion ==3 and caverna.get_cerrojo_caverna(1).vida_cerrojo == 0.0:
            eleccion = int(input(
                "El nombre del mejor equipo por el momento es: \n\n" +
                equipo[mejor_posicion].nombre_equipo +
                "\n\n\n1.Seguir jugando\n2. Abandonar el juego"))
        elif mejor_posicion == 0 and eleccion == 3 and caverna.get_cerrojo_caverna(1).vida_cerrojo > 0.0:
                print("No hay registro aun, ningun equipo a pasado la primera Caverna")
                eleccion = int(input(
                    "Resumen del juego: \n" +
                    caverna.__str__() + "\n" +
                    "Numero de hechizos realizados " + str(hechizo.get_contador_hechizo()) + "\n" +
                    equipo.__str__() + "\n\n\n" +
                    "1. Hacer un hechizo\n2. Abandonar el Juego\n"))
        return eleccion

    def destruir_cerrojo(self):
        """
        Nivel donde se destruye el cerrojo de la caverna

        Returns:
        None
        """
        return None

juego = Juego()
juego.correr()
