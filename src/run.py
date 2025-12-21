import sys

class InterfazGUI:
    # Placeholder for GUI interface methods
    def solicitarInt(self, message):
        # This should be implemented to request an integer from the GUI
        print(f"GUI Request Int: {message}")
        # For console testing, you can use input() or a default value
        return int(input("Enter integer (GUI): "))

class InterfazConsola:
    # Placeholder for Console interface methods
    def solicitarInt(self, message):
        print(message)
        # In a real scenario, this would handle input validation.
        return int(input("Enter integer: "))

    def solicitarString(self, message):
        print(message)
        return input("Enter string: ")

    def solicitarDouble(self, message):
        print(message)
        # In a real scenario, this would handle input validation.
        return float(input("Enter double: "))

    def mostrarMensaje(self, message):
        print("\n" + "="*50)
        print("MESSAGE:")
        print(message)
        print("="*50 + "\n")

# Minimal placeholder classes for structure
class Hechizo:
    def __init__(self):
        self._contador_hechizo = 0
        self._segundos_hechizo = 0.0

    def getContadorHechizo(self):
        return self._contador_hechizo

    def setContadorHechizo(self, count):
        self._contador_hechizo = count

    def setSegundosHechizo(self, seconds):
        self._segundos_hechizo = seconds

    def vidaEnfrentamientoJugadorCerrojo(self, jugador, cerrojo, gema_jugador_choice, gema_cerrojo_choice):
        # *** YOU MUST IMPLEMENT THE GAME LOGIC HERE ***
        # This is where the core battle/puzzle logic happens.
        pass

class Gema:
    def __init__(self):
        self._vida = 100.0 # Placeholder value

    def getVidaGema(self):
        return self._vida
    
    # You would need setVidaGema if it's used elsewhere

class Jugador:
    def __init__(self, name):
        self._name = name
        self._vivo = True
        # Assuming Jugador has a list/array of 3 Gemas
        self._gemas = [Gema(), Gema(), Gema()]

    def getVidaJugador(self):
        return self._vivo

    def setVidaJugador(self, alive):
        self._vivo = alive

    def toStringJugador(self):
        return f"Jugador: {self._name} (Vivo: {self._vivo})"

    def getGemaJugador(self, index):
        # Python uses 0-based indexing, but the Java code uses 1-based indexing
        # We adjust here to handle the Java code's 1-based index (1, 2, 3)
        return self._gemas[index - 1]

class Cerrojo:
    def __init__(self):
        self._vivo = True
        # Assuming Cerrojo has a list/array of 3 Gemas
        self._gemas = [Gema(), Gema(), Gema()]

    def getVida(self):
        return self._vivo

    def setVida(self, alive):
        self._vivo = alive

    def toStringCerrojo(self):
        # *** YOU MUST IMPLEMENT THE ACTUAL TOSTRING LOGIC HERE ***
        return "Cerrojo Status Placeholder: [G1, G2, G3]"

    def getGemaCerrojo(self, index):
        # Python uses 0-based indexing, but the Java code uses 1-based indexing
        # We adjust here to handle the Java code's 1-based index (1, 2, 3)
        return self._gemas[index - 1]

class Caverna:
    def __init__(self):
        # Assuming Caverna has a list/array of 3 Cerrojos
        self._cerrojos = [Cerrojo(), Cerrojo(), Cerrojo()]
        # Assuming Caverna has oxygen and letality levels for each level
        self._oxigeno = [10.0, 10.0, 10.0] # Placeholder for 3 levels (Caverna 1, 2, 3)
        self._letalidad = [0.2, 0.3, 0.4] # Placeholder

    def toStringCaverna(self, level_index):
        # *** YOU MUST IMPLEMENT THE ACTUAL TOSTRING LOGIC HERE ***
        return f"Caverna {level_index} Status Placeholder: Oxygen={self._oxigeno[level_index-1]}"
    
    def toString(self):
        # *** YOU MUST IMPLEMENT THE ACTUAL TOSTRING LOGIC HERE ***
        return "Caverna Full Status Placeholder"

    def getCerrojoCaverna(self, index):
        # Python uses 0-based indexing, but the Java code uses 1-based indexing
        # We adjust here to handle the Java code's 1-based index (1, 2, 3)
        return self._cerrojos[index - 1]

    def getOxigenoCaverna(self, index):
        return self._oxigeno[index - 1]

    def setOxigenoCaverna(self, index, letalidad):
        # Placeholder logic: Oxygen is reduced by letalidad
        self._oxigeno[index - 1] -= letalidad

    def getLetalidadCaverna(self, index):
        return self._letalidad[index - 1]

    def setLetalidadCaverna(self, new_letalidad, index):
        self._letalidad[index - 1] = new_letalidad

class Equipo:
    def __init__(self, name, j1, j2, j3, is_alive):
        self._name = name
        self._jugadores = [j1, j2, j3]
        self._vivo = is_alive

    def getNombreEquipo(self):
        return self._name

    def toStringEquipo(self):
        # *** YOU MUST IMPLEMENT THE ACTUAL TOSTRING LOGIC HERE ***
        return f"Equipo: {self._name} (Vivo: {self._vivo}, J1, J2, J3...)"

    def getVivoEquipo(self):
        return self._vivo

    def setVivoEquipo(self, is_alive):
        self._vivo = is_alive

    def getJugadorEquipo(self, index):
        # Python uses 0-based indexing, but the Java code uses 1-based indexing
        # We adjust here to handle the Java code's 1-based index (1, 2, 3)
        return self._jugadores[index - 1]

# ==============================================================================
# TRANSLATED CLASS
# ==============================================================================

class ScapeRoomC:
    """
    Translated Python class from Java's ScapeRoomC.
    Note: Requires the logic in the placeholder classes above to function correctly.
    """
    
    # Class attributes (similar to Java class fields)
    mejor_posicion = 0
    interfaz_gui = None # Will not be used in this console-based translation
    interfaz_c = None
    hechizo = None
    equipo = None # Array/List of Equipo objects
    caverna = None # Array/List of Caverna objects
    jugador = None # Array/List of Jugador objects (used temporarily)
    segundos_hechizo = 0.0

    def __init__(self):
        """constructor vacio"""
        pass

    def run(self):
        """metodo para correr la aplicacion y mostrarla en GUI"""
        self.interfaz_c = InterfazConsola()
        
        # Java array size is fixed, Python uses lists
        cuantos_equipos = self.interfaz_c.solicitarInt("Cuantos Equipos participan en el torneo de \n\nSCAPE ROOM SUBTERRANEO? ")
        
        self.equipo = [None] * cuantos_equipos
        self.caverna = [None] * cuantos_equipos

        for i in range(cuantos_equipos):
            # SE REINICIAN CADA FOR
            contador_gemas_muertas1 = 0
            contador_gemas_muertas2 = 0
            contador_gemas_muertas3 = 0
            contador_jugador_muerto = 0
            no_hay_un_muerto = True
            no_hay_dos_muertos = True
            
            self.hechizo = Hechizo()
            self.jugador = [None] * 3 # List of 3 players for the current team

            nombre_equipo = self.interfaz_c.solicitarString(f"Nombre del Equipo: {i+1}\n")
            
            for j in range(3):
                nombre_jugador = self.interfaz_c.solicitarString(f"Nombre del jugador: {j+1}\n")
                self.jugador[j] = Jugador(nombre_jugador)

            # Assign team name and players (j0, j1, j2)
            self.equipo[i] = Equipo(nombre_equipo, self.jugador[0], self.jugador[1], self.jugador[2], True)
            self.caverna[i] = Caverna()

            # Elige que hacer el equipo antes de entrar a caverna:
            menu_text = (
                f"Resumen del juego: \n{self.caverna[i].toStringCaverna(i+1)}\n"
                f"Numero de hechizos realizados {self.hechizo.getContadorHechizo()}\n"
                f"{self.equipo[i].toStringEquipo()}\n\n\n"
                "1. Hacer un hechizo\n2. Abandonar el Juego\n3. Historial del juego"
            )
            eleccion = self.interfaz_c.solicitarInt(menu_text)

            # NOTE: Java uses break labels (Caverna1:, Caverna2:, Caverna3:). 
            # In Python, we simulate this with flags, nested loops, or by using a function/method
            # and 'return'. Since this is a direct translation of a loop block, we'll
            # use a simple flag/state for control, but a refactored version should use functions.

            # Historial check block
            if self.mejor_posicion != 0 and eleccion == 3:
                eleccion = self.interfaz_c.solicitarInt(
                    f"El nombre del mejor equipo por el momento es: \n\n{self.equipo[self.mejor_posicion].getNombreEquipo()}\n\n\n"
                    "1.Seguir jugando\n2. Abandonar el juego"
                )
            # The next two conditions check index 1 (1-based) which is Cerrojo 1
            elif self.mejor_posicion == 0 and eleccion == 3 and self.caverna[i].getCerrojoCaverna(1).getVida() == False:
                # The original code re-uses self.mejor_posicion = 0 here, which is likely a bug/oversight
                # as it points to the current team or the first team if it won Caverna 1.
                eleccion = self.interfaz_c.solicitarInt(
                    f"El nombre del mejor equipo por el momento es: \n\n{self.equipo[self.mejor_posicion].getNombreEquipo()}\n\n\n"
                    "1.Seguir jugando\n2. Abandonar el juego"
                )
            elif self.mejor_posicion == 0 and eleccion == 3 and self.caverna[i].getCerrojoCaverna(1).getVida() == True:
                self.interfaz_c.mostrarMensaje("No hay registro aun, ningun equipo a pasado la primera Caverna")
                eleccion = self.interfaz_c.solicitarInt(
                    f"Resumen del juego: \n{self.caverna[i].toStringCaverna(i+1)}\n"
                    f"Numero de hechizos realizados {self.hechizo.getContadorHechizo()}\n"
                    f"{self.equipo[i].toStringEquipo()}\n\n\n"
                    "1. Hacer un hechizo\n2. Abandonar el Juego\n"
                )
            
            # --- START CAVERNA 1 LOOP BLOCK ---
            caverna1_finished = False
            self.hechizo.setContadorHechizo(0)
            while eleccion == 1 and self.caverna[i].getOxigenoCaverna(1) > 0.0 and self.equipo[i].getVivoEquipo():
                eleccion_gema_jugador = 1
                self.segundos_hechizo = 1.0 # Re-uses the class attribute
                eleccion_gema_cerrojo = 1

                # pregunta por CUANTOS SEGUNDOS POR HECHIZO GRUPAL
                self.segundos_hechizo = self.interfaz_c.solicitarDouble(f"Segundos del hechizo del Equipo {i+1}:\n")
                self.hechizo.setSegundosHechizo(self.segundos_hechizo)

                # JUGADOR 1
                if self.equipo[i].getJugadorEquipo(1).getVidaJugador():
                    eleccion_gema_jugador = self.interfaz_c.solicitarInt(
                        f"{self.equipo[i].getJugadorEquipo(1).toStringJugador()}\n\n1. Gema FUEGO\n2. Gema AGUA\n3. Gema METAL \n"
                    )
                    eleccion_gema_cerrojo = self.interfaz_c.solicitarInt(
                        f"{self.caverna[i].getCerrojoCaverna(1).toStringCerrojo()}\n\n1. Primera Gema\n2. Segunda Gema\n3. Tercera Gema\n"
                    )
                    # HACEMOS UN HECHIZO JUGADOR 1
                    self.hechizo.vidaEnfrentamientoJugadorCerrojo(
                        self.equipo[i].getJugadorEquipo(1), self.caverna[i].getCerrojoCaverna(1), 
                        eleccion_gema_jugador, eleccion_gema_cerrojo
                    )
                    # CONDICIONES PARA SABER SI JUGADOR 1 SIGUE VIVO
                    j1 = self.equipo[i].getJugadorEquipo(1)
                    if j1.getGemaJugador(1).getVidaGema() <= 0.0 and j1.getGemaJugador(2).getVidaGema() <= 0.0 and j1.getGemaJugador(3).getVidaGema() <= 0.0:
                        contador_gemas_muertas1 = 3
                    if contador_gemas_muertas1 == 3:
                        j1.setVidaJugador(False)
                        contador_jugador_muerto += 1

                # JUGADOR 2
                if self.equipo[i].getJugadorEquipo(2).getVidaJugador():
                    eleccion_gema_jugador = self.interfaz_c.solicitarInt(
                        f"{self.equipo[i].getJugadorEquipo(2).toStringJugador()}\n\n1. Gema FUEGO\n2. Gema AGUA\n3. Gema METAL \n"
                    )
                    eleccion_gema_cerrojo = self.interfaz_c.solicitarInt(
                        f"{self.caverna[i].getCerrojoCaverna(1).toStringCerrojo()}\n\n1. Primera Gema\n2. Segunda Gema\n3. Tercera Gema\n"
                    )
                    # HACEMOS UN HECHIZO JUGADOR 2
                    self.hechizo.vidaEnfrentamientoJugadorCerrojo(
                        self.equipo[i].getJugadorEquipo(2), self.caverna[i].getCerrojoCaverna(1), 
                        eleccion_gema_jugador, eleccion_gema_cerrojo
                    )
                    # CONDICIONES PARA SABER SI JUGADOR 2 SIGUE VIVO
                    j2 = self.equipo[i].getJugadorEquipo(2)
                    if j2.getGemaJugador(1).getVidaGema() <= 0.0 and j2.getGemaJugador(2).getVidaGema() <= 0.0 and j2.getGemaJugador(3).getVidaGema() <= 0.0:
                        contador_gemas_muertas2 = 3
                    if contador_gemas_muertas2 == 3:
                        j2.setVidaJugador(False)
                        contador_jugador_muerto += 1

                # JUGADOR 3
                if self.equipo[i].getJugadorEquipo(3).getVidaJugador():
                    eleccion_gema_jugador = self.interfaz_c.solicitarInt(
                        f"{self.equipo[i].getJugadorEquipo(3).toStringJugador()}\n\n1. Gema FUEGO\n2. Gema AGUA\n3. Gema METAL \n"
                    )
                    eleccion_gema_cerrojo = self.interfaz_c.solicitarInt(
                        f"{self.caverna[i].getCerrojoCaverna(1).toStringCerrojo()}\n\n1. Primera Gema\n2. Segunda Gema\n3. Tercera Gema\n"
                    )
                    # HACEMOS UN HECHIZO JUGADOR 3
                    self.hechizo.vidaEnfrentamientoJugadorCerrojo(
                        self.equipo[i].getJugadorEquipo(3), self.caverna[i].getCerrojoCaverna(1), 
                        eleccion_gema_jugador, eleccion_gema_cerrojo
                    )
                    # CONDICIONES PARA SABER SI JUGADOR 3 SIGUE VIVO
                    j3 = self.equipo[i].getJugadorEquipo(3)
                    if j3.getGemaJugador(1).getVidaGema() <= 0.0 and j3.getGemaJugador(2).getVidaGema() <= 0.0 and j3.getGemaJugador(3).getVidaGema() <= 0.0:
                        contador_gemas_muertas3 = 3
                    if contador_gemas_muertas3 == 3:
                        j3.setVidaJugador(False)
                        contador_jugador_muerto += 1

                self.hechizo.setContadorHechizo(1) # contador de hechizos por ataque Grupal

                # LETALIDAD ADJUSTMENTS
                if contador_jugador_muerto == 1 and no_hay_un_muerto:
                    self.caverna[i].setLetalidadCaverna(0.2 / 2, 1)
                    no_hay_un_muerto = False
                
                if contador_jugador_muerto == 2 and no_hay_dos_muertos:
                    self.caverna[i].setLetalidadCaverna(0.2 / 4, 1)
                    no_hay_dos_muertos = False

                # OXYGEN CHANGE
                self.caverna[i].setOxigenoCaverna(1, self.caverna[i].getLetalidadCaverna(1))

                # CONDICIONES DE PERDER EN CAVERNA 1 (Oxygen)
                if self.caverna[i].getOxigenoCaverna(1) <= 0.0:
                    self.interfaz_c.mostrarMensaje(
                        f"GAME OVER!\n\nLos jugadores se quedaron sin oxigeno!\n\n{self.equipo[i].toStringEquipo()}\n\n"
                        f"Numero de hechizos realizados {self.hechizo.getContadorHechizo()}\n"
                        f"El oxeno de la caverna 1: {self.caverna[i].getOxigenoCaverna(1)}"
                    )
                    caverna1_finished = True
                    break # break Caverna1

                # CONDICIONES DE PERDER EN CAVERNA 1 (All Players Dead)
                if contador_jugador_muerto == 3:
                    self.equipo[i].setVivoEquipo(False)

                if not self.equipo[i].getVivoEquipo():
                    self.interfaz_c.mostrarMensaje(
                        f"Todos los jugadores estan muertos\n :(\n\n{self.equipo[i].toStringEquipo()}\n\n{self.caverna[i].toString()}"
                    )
                    caverna1_finished = True
                    break # break Caverna1

                # CONDICIONES DE GANAR EL PRIMER NIVEL
                cerrojo1 = self.caverna[i].getCerrojoCaverna(1)
                if cerrojo1.getGemaCerrojo(1).getVidaGema() <= 0.0 and cerrojo1.getGemaCerrojo(2).getVidaGema() <= 0.0 and cerrojo1.getGemaCerrojo(3).getVidaGema() <= 0.0:
                    cerrojo1.setVida(False)

                if not cerrojo1.getVida():
                    eleccion = self.interfaz_c.solicitarInt(
                        f"FELICIDADES LOS JUGADORES PASAN A LA SIGUIENTE CAVERNA\n\n"
                        f"Numero de hechizos realizados {self.hechizo.getContadorHechizo()}\n"
                        f"{self.equipo[i].toStringEquipo()}\n\n"
                        f"{cerrojo1.toStringCerrojo()}1. Seguir jugando\n2. Abandonar el Juego"
                    )
                    self.mejor_posicion = i
                    caverna1_finished = True
                    break # break Caverna1

                # RESUMEN DEL JUEGO LUEGO DE LAS ELECCIONES DE LAS GEMAS
                eleccion = self.interfaz_c.solicitarInt(
                    f"Resumen del juego: \n{self.caverna[i].toStringCaverna(1)}\n"
                    f"Numero de hechizos realizados {self.hechizo.getContadorHechizo()}\n"
                    f"{self.equipo[i].toStringEquipo()}\n\n\n"
                    "1. Hacer un hechizo\n2. Abandonar el Juego"
                )

                # CONDICION DE SALIR DE LA CAVERNA ANTES DE TIEMPO
                if eleccion == 2:
                    caverna1_finished = True
                    break # break Caverna1
            
            # If the loop finished due to a break condition that wasn't 'win' or 'continue' (like abandon), skip to next team
            if eleccion != 1 or not self.equipo[i].getVivoEquipo() or self.caverna[i].getOxigenoCaverna(1) <= 0.0:
                continue

            # --- START CAVERNA 2 LOOP BLOCK ---
            caverna2_finished = False
            self.hechizo.setContadorHechizo(0)
            while eleccion == 1 and self.caverna[i].getOxigenoCaverna(1) > 0.0 and self.equipo[i].getVivoEquipo() and self.caverna[i].getOxigenoCaverna(2) > 0.0:
                eleccion_gema_jugador = 1
                segundos_hechizo = 1.0
                eleccion_gema_cerrojo = 1

                # pregunta por CUANTOS SEGUNDOS POR HECHIZO GRUPAL
                segundos_hechizo = self.interfaz_c.solicitarDouble(f"Segundos del hechizo del Equipo {i+1}:\n")
                self.hechizo.setSegundosHechizo(segundos_hechizo)

                # JUGADOR 1 (Logic repeats from Caverna 1, targeting Cerrojo 2 and using letality 0.3)
                if self.equipo[i].getJugadorEquipo(1).getVidaJugador():
                    eleccion_gema_jugador = self.interfaz_c.solicitarInt(f"{self.equipo[i].getJugadorEquipo(1).toStringJugador()}\n\n1. Gema FUEGO\n2. Gema AGUA\n3. Gema METAL \n")
                    eleccion_gema_cerrojo = self.interfaz_c.solicitarInt(f"{self.caverna[i].getCerrojoCaverna(2).toStringCerrojo()}\n\n1. Primera Gema\n2. Segunda Gema\n3. Tercera Gema\n")
                    self.hechizo.vidaEnfrentamientoJugadorCerrojo(self.equipo[i].getJugadorEquipo(1), self.caverna[i].getCerrojoCaverna(2), eleccion_gema_jugador, eleccion_gema_cerrojo)
                    # ... (Vida check for J1)
                    j1 = self.equipo[i].getJugadorEquipo(1)
                    if j1.getGemaJugador(1).getVidaGema() <= 0.0 and j1.getGemaJugador(2).getVidaGema() <= 0.0 and j1.getGemaJugador(3).getVidaGema() <= 0.0:
                        contador_gemas_muertas1 = 3
                    if contador_gemas_muertas1 == 3:
                        j1.setVidaJugador(False)
                        contador_jugador_muerto += 1
                
                # JUGADOR 2 (Logic repeats, targeting Cerrojo 2)
                if self.equipo[i].getJugadorEquipo(2).getVidaJugador():
                    eleccion_gema_jugador = self.interfaz_c.solicitarInt(f"{self.equipo[i].getJugadorEquipo(2).toStringJugador()}\n\n1. Gema FUEGO\n2. Gema AGUA\n3. Gema METAL \n")
                    eleccion_gema_cerrojo = self.interfaz_c.solicitarInt(f"{self.caverna[i].getCerrojoCaverna(2).toStringCerrojo()}\n\n1. Primera Gema\n2. Segunda Gema\n3. Tercera Gema\n")
                    self.hechizo.vidaEnfrentamientoJugadorCerrojo(self.equipo[i].getJugadorEquipo(2), self.caverna[i].getCerrojoCaverna(2), eleccion_gema_jugador, eleccion_gema_cerrojo)
                    # ... (Vida check for J2)
                    j2 = self.equipo[i].getJugadorEquipo(2)
                    if j2.getGemaJugador(1).getVidaGema() <= 0.0 and j2.getGemaJugador(2).getVidaGema() <= 0.0 and j2.getGemaJugador(3).getVidaGema() <= 0.0:
                        contador_gemas_muertas2 = 3
                    if contador_gemas_muertas2 == 3:
                        j2.setVidaJugador(False)
                        contador_jugador_muerto += 1

                # JUGADOR 3 (Logic repeats, targeting Cerrojo 2)
                if self.equipo[i].getJugadorEquipo(3).getVidaJugador():
                    eleccion_gema_jugador = self.interfaz_c.solicitarInt(f"{self.equipo[i].getJugadorEquipo(3).toStringJugador()}\n\n1. Gema FUEGO\n2. Gema AGUA\n3. Gema METAL \n")
                    eleccion_gema_cerrojo = self.interfaz_c.solicitarInt(f"{self.caverna[i].getCerrojoCaverna(2).toStringCerrojo()}\n\n1. Primera Gema\n2. Segunda Gema\n3. Tercera Gema\n")
                    self.hechizo.vidaEnfrentamientoJugadorCerrojo(self.equipo[i].getJugadorEquipo(3), self.caverna[i].getCerrojoCaverna(2), eleccion_gema_jugador, eleccion_gema_cerrojo)
                    # ... (Vida check for J3)
                    j3 = self.equipo[i].getJugadorEquipo(3)
                    if j3.getGemaJugador(1).getVidaGema() <= 0.0 and j3.getGemaJugador(2).getVidaGema() <= 0.0 and j3.getGemaJugador(3).getVidaGema() <= 0.0:
                        contador_gemas_muertas3 = 3
                    if contador_gemas_muertas3 == 3:
                        j3.setVidaJugador(False)
                        contador_jugador_muerto += 1

                self.hechizo.setContadorHechizo(1) # contador de hechizos por ataque Grupal

                # LETALIDAD ADJUSTMENTS for Caverna 2
                if contador_jugador_muerto == 1 and no_hay_un_muerto:
                    self.caverna[i].setLetalidadCaverna(0.3 / 2, 2)
                    no_hay_un_muerto = False
                
                if contador_jugador_muerto == 2 and no_hay_dos_muertos:
                    self.caverna[i].setLetalidadCaverna(0.3 / 4, 2)
                    no_hay_dos_muertos = False

                self.caverna[i].setOxigenoCaverna(2, self.caverna[i].getLetalidadCaverna(2))

                # CONDICIONES DE PERDER EN CAVERNA 2 (Oxygen)
                if self.caverna[i].getOxigenoCaverna(2) <= 0.0:
                    self.interfaz_c.mostrarMensaje(
                        f"GAME OVER!\n\nLos jugadores se quedaron sin oxigeno!\n\n"
                        f"Numero de hechizos realizados {self.hechizo.getContadorHechizo()}\n"
                        f"{self.equipo[i].toStringEquipo()} \n\n{self.caverna[i].toString()}"
                    )
                    caverna2_finished = True
                    break

                # CONDICIONES DE PERDER EN CAVERNA 2 (All Players Dead)
                if contador_jugador_muerto == 3:
                    self.equipo[i].setVivoEquipo(False)
                
                if not self.equipo[i].getVivoEquipo():
                    self.interfaz_c.mostrarMensaje(
                        f"Todos los jugadores estan muertos\n :(\n\n"
                        f"Numero de hechizos realizados {self.hechizo.getContadorHechizo()}\n"
                        f"{self.equipo[i].toStringEquipo()}\n\n{self.caverna[i].toString()}"
                    )
                    caverna2_finished = True
                    break

                # CONDICIONES DE GANAR EL SEGUNDO NIVEL
                cerrojo2 = self.caverna[i].getCerrojoCaverna(2)
                if cerrojo2.getGemaCerrojo(1).getVidaGema() <= 0.0 and cerrojo2.getGemaCerrojo(2).getVidaGema() <= 0.0 and cerrojo2.getGemaCerrojo(3).getVidaGema() <= 0.0:
                    cerrojo2.setVida(False)

                if not cerrojo2.getVida():
                    eleccion = self.interfaz_c.solicitarInt(
                        f"FELICIDADES LOS JUGADORES PASAN A LA SIGUIENTE CAVERNA\n\n"
                        f"Numero de hechizos realizados {self.hechizo.getContadorHechizo()}\n"
                        f"{self.equipo[i].toStringEquipo()}\n\n"
                        f"{cerrojo2.toStringCerrojo()}1. Seguir jugando\n2. Abandonar el Juego"
                    )
                    self.mejor_posicion = i
                    caverna2_finished = True
                    break

                # RESUMEN DEL JUEGO LUEGO DE LAS ELECCIONES DE LAS GEMAS
                eleccion = self.interfaz_c.solicitarInt(
                    f"Resumen del juego: \n{self.caverna[i].toStringCaverna(2)}\n"
                    f"Numero de hechizos realizados {self.hechizo.getContadorHechizo()}\n"
                    f"{self.equipo[i].toStringEquipo()}\n\n\n"
                    "1. Hacer un hechizo\n2. Abandonar el Juego"
                )

                # CONDICION DE SALIR DE LA CAVERNA ANTES DE TIEMPO
                if eleccion == 2:
                    caverna2_finished = True
                    break
            
            if eleccion != 1 or not self.equipo[i].getVivoEquipo() or self.caverna[i].getOxigenoCaverna(2) <= 0.0:
                continue

            # --- START CAVERNA 3 LOOP BLOCK ---
            caverna3_finished = False
            self.hechizo.setContadorHechizo(0)
            while eleccion == 1 and self.caverna[i].getOxigenoCaverna(1) > 0.0 and self.equipo[i].getVivoEquipo() and self.caverna[i].getOxigenoCaverna(2) > 0.0 and self.caverna[i].getOxigenoCaverna(3) > 0.0:
                eleccion_gema_jugador = 1
                segundos_hechizo = 1.0
                eleccion_gema_cerrojo = 1

                # pregunta por CUANTOS SEGUNDOS POR HECHIZO GRUPAL
                segundos_hechizo = self.interfaz_c.solicitarDouble(f"Segundos del hechizo del Equipo {i+1}:\n")
                self.hechizo.setSegundosHechizo(segundos_hechizo)

                # NOTE: The original Java code switched to `interfazGUI.solicitarInt` for J3 here. 
                # Assuming this was a typo and should be `interfazC.solicitarInt` for a console-based app.
                
                # JUGADOR 1 (Logic repeats, targeting Cerrojo 3 and using letality 0.4)
                if self.equipo[i].getJugadorEquipo(1).getVidaJugador():
                    # ... (Input and Hechizo logic)
                    eleccion_gema_jugador = self.interfaz_c.solicitarInt(f"{self.equipo[i].getJugadorEquipo(1).toStringJugador()}\n\n1. Gema FUEGO\n2. Gema AGUA\n3. Gema METAL \n")
                    eleccion_gema_cerrojo = self.interfaz_c.solicitarInt(f"{self.caverna[i].getCerrojoCaverna(3).toStringCerrojo()}\n\n1. Primera Gema\n2. Segunda Gema\n3. Tercera Gema\n")
                    self.hechizo.vidaEnfrentamientoJugadorCerrojo(self.equipo[i].getJugadorEquipo(1), self.caverna[i].getCerrojoCaverna(3), eleccion_gema_jugador, eleccion_gema_cerrojo)
                    # ... (Vida check for J1)
                    j1 = self.equipo[i].getJugadorEquipo(1)
                    if j1.getGemaJugador(1).getVidaGema() <= 0.0 and j1.getGemaJugador(2).getVidaGema() <= 0.0 and j1.getGemaJugador(3).getVidaGema() <= 0.0:
                        contador_gemas_muertas1 = 3
                    if contador_gemas_muertas1 == 3:
                        j1.setVidaJugador(False)
                        contador_jugador_muerto += 1

                # JUGADOR 2 (Logic repeats, targeting Cerrojo 3)
                if self.equipo[i].getJugadorEquipo(2).getVidaJugador():
                    # ... (Input and Hechizo logic)
                    eleccion_gema_jugador = self.interfaz_c.solicitarInt(f"{self.equipo[i].getJugadorEquipo(2).toStringJugador()}\n\n1. Gema FUEGO\n2. Gema AGUA\n3. Gema METAL \n")
                    eleccion_gema_cerrojo = self.interfaz_c.solicitarInt(f"{self.caverna[i].getCerrojoCaverna(3).toStringCerrojo()}\n\n1. Primera Gema\n2. Segunda Gema\n3. Tercera Gema\n")
                    self.hechizo.vidaEnfrentamientoJugadorCerrojo(self.equipo[i].getJugadorEquipo(2), self.caverna[i].getCerrojoCaverna(3), eleccion_gema_jugador, eleccion_gema_cerrojo)
                    # ... (Vida check for J2)
                    j2 = self.equipo[i].getJugadorEquipo(2)
                    if j2.getGemaJugador(1).getVidaGema() <= 0.0 and j2.getGemaJugador(2).getVidaGema() <= 0.0 and j2.getGemaJugador(3).getVidaGema() <= 0.0:
                        contador_gemas_muertas2 = 3
                    if contador_gemas_muertas2 == 3:
                        j2.setVidaJugador(False)
                        contador_jugador_muerto += 1

                # JUGADOR 3 (Logic repeats, targeting Cerrojo 3)
                if self.equipo[i].getJugadorEquipo(3).getVidaJugador():
                    # Correcting the likely typo from interfazGUI to interfazC for console
                    eleccion_gema_jugador = self.interfaz_c.solicitarInt(f"{self.equipo[i].getJugadorEquipo(3).toStringJugador()}\n\n1. Gema FUEGO\n2. Gema AGUA\n3. Gema METAL \n")
                    eleccion_gema_cerrojo = self.interfaz_c.solicitarInt(f"{self.caverna[i].getCerrojoCaverna(3).toStringCerrojo()}\n\n1. Primera Gema\n2. Segunda Gema\n3. Tercera Gema\n")
                    self.hechizo.vidaEnfrentamientoJugadorCerrojo(self.equipo[i].getJugadorEquipo(3), self.caverna[i].getCerrojoCaverna(3), eleccion_gema_jugador, eleccion_gema_cerrojo)
                    # ... (Vida check for J3)
                    j3 = self.equipo[i].getJugadorEquipo(3)
                    if j3.getGemaJugador(1).getVidaGema() <= 0.0 and j3.getGemaJugador(2).getVidaGema() <= 0.0 and j3.getGemaJugador(3).getVidaGema() <= 0.0:
                        contador_gemas_muertas3 = 3
                    if contador_gemas_muertas3 == 3:
                        j3.setVidaJugador(False)
                        contador_jugador_muerto += 1

                self.hechizo.setContadorHechizo(1) # contador de hechizos por ataque Grupal

                # LETALIDAD ADJUSTMENTS for Caverna 3
                if contador_jugador_muerto == 1 and no_hay_un_muerto:
                    self.caverna[i].setLetalidadCaverna(0.4 / 2, 3)
                    no_hay_un_muerto = False
                
                if contador_jugador_muerto == 2 and no_hay_dos_muertos:
                    self.caverna[i].setLetalidadCaverna(0.4 / 4, 3)
                    no_hay_dos_muertos = False

                self.caverna[i].setOxigenoCaverna(3, self.caverna[i].getLetalidadCaverna(3))

                # CONDICIONES DE PERDER EN CAVERNA 3 (Oxygen)
                if self.caverna[i].getOxigenoCaverna(3) <= 0.0:
                    self.interfaz_c.mostrarMensaje(
                        f"GAME OVER!\n\nLos jugadores se quedaron sin oxigeno!\n\n"
                        f"Numero de hechizos realizados {self.hechizo.getContadorHechizo()}\n"
                        f"{self.equipo[i].toStringEquipo()} \n\n{self.caverna[i].toString()}"
                    )
                    caverna3_finished = True
                    break

                # CONDICIONES DE PERDER EN CAVERNA 3 (All Players Dead)
                if contador_jugador_muerto == 3:
                    self.equipo[i].setVivoEquipo(False)
                
                if not self.equipo[i].getVivoEquipo():
                    self.interfaz_c.mostrarMensaje(
                        f"Todos los jugadores estan muertos\n :(\n\n"
                        f"Numero de hechizos realizados {self.hechizo.getContadorHechizo()}\n"
                        f"{self.equipo[i].toStringEquipo()}\n\n{self.caverna[i].toString()}"
                    )
                    caverna3_finished = True
                    break

                # CONDICIONES DE GANAR EL TERCER NIVEL (GAME WIN)
                cerrojo3 = self.caverna[i].getCerrojoCaverna(3)
                if cerrojo3.getGemaCerrojo(1).getVidaGema() <= 0.0 and cerrojo3.getGemaCerrojo(2).getVidaGema() <= 0.0 and cerrojo3.getGemaCerrojo(3).getVidaGema() <= 0.0:
                    cerrojo3.setVida(False)

                if not cerrojo3.getVida():
                    # The original Java code ends abruptly here, assuming the final WIN message is displayed.
                    self.interfaz_c.mostrarMensaje(f"FELICIDADES LOS JUGADORES GANARON EL JUEGO! \n\n{self.equipo[i].toStringEquipo()}\n")
                    self.mejor_posicion = i
                    caverna3_finished = True
                    break # Break the while loop

                # RESUMEN DEL JUEGO LUEGO DE LAS ELECCIONES DE LAS GEMAS
                # This part is omitted as the Java code seems to cut off before the loop continues
                # eleccion = self.interfaz_c.solicitarInt(...)

                # CONDICION DE SALIR DE LA CAVERNA ANTES DE TIEMPO
                # if eleccion == 2: break
            
            # --- END CAVERNA 3 LOOP BLOCK ---

# Example of how to run the game:
# if __name__ == "__main__":
#     game = ScapeRoomC()
#     game.run()