import Cerrojo

class Caverna:
    def __init__(self):
        """
        Inicializa una instancia de Caverna.

        La caverna contiene tres cerraduras (cerrojos), cada una con su
        propio estado de oxígeno, letalidad y puertas.
        """
        self.nombre_cerrojo = ["Cerrojo 1", "Cerrojo 2", "Cerrojo 3"]
        self.letalidad_caverna = [0.2, 0.3, 0.4]
        self.cerrojo_caverna = [None] * 3
        self.oxigeno_caverna = [1.0] * 3

        for i in range(3):
            self.cerrojo_caverna[i] = Cerrojo.Cerrojo(self.nombre_cerrojo[i])

    def set_oxigeno_jugador_caverna(self, jugador, oxigeno, cual_caverna):
        """
        Establece el nivel de oxígeno para un jugador en una caverna específica.

        Args:
            jugador (Jugador): El jugador al que se le establecerá el nivel de oxígeno.
            oxigeno (float): El nivel de oxígeno a establecer.
            cual_caverna (int): El número de la caverna (1, 2 o 3).

        Returns:
            None
        """
        try:
            self.oxigeno_caverna[cual_caverna - 1] = oxigeno
            jugador.set_oxigeno_jugador(self.oxigeno_caverna[cual_caverna - 1])
        except IndexError:
            print("Indice de caverna fuera de rango.")

    def set_oxigeno_caverna(self, cual_caverna, oxigeno):
        """
        Reduce el nivel de oxígeno en una caverna específica.

        Args:
            cual_caverna (int): El número de la caverna (1, 2 o 3).
            oxigeno (float): La cantidad de oxígeno a reducir.

        Returns:
            None
        """
        try:
            self.oxigeno_caverna[cual_caverna - 1] -= oxigeno
        except IndexError:
            print("Indice de caverna fuera de rango.")


    def get_oxigeno_caverna(self, cual_caverna):
        """
        Obtiene el nivel de oxígeno en una caverna específica.

        Args:
            cual_caverna (int): El número de la caverna (1, 2 o 3).

        Returns:
            float: El nivel de oxígeno en la caverna.
        """
        try:
            return self.oxigeno_caverna[cual_caverna - 1]
        except IndexError:
            print("Indice de caverna fuera de rango.")

    def get_cerrojo_caverna(self, cual_cerrojo):
        """
        Obtiene una cerradura (cerrojo) en la caverna por su número (1, 2 o 3).

        Args:
            cual_cerrojo (int): El número de la cerradura deseada (1, 2 o 3).

        Returns:
            Cerrojo: La cerradura seleccionada.
        """
        try:
            if cual_cerrojo+1 == 1:
                return self.cerrojo_caverna[0]
            elif cual_cerrojo+1 == 2:
                return self.cerrojo_caverna[1]
            elif cual_cerrojo+1 == 3:
                return self.cerrojo_caverna[2]
            else:
                return None
        except IndexError:
            print("Índice de gema fuera de rango. La caverna no tiene esa gema.")
            return None

    def set_cerrojo_caverna(self, puerta, cual_cerrojo):
        """
        Establece una cerradura (cerrojo) en la caverna por su número (1, 2 o 3).

        Args:
            puerta (Cerrojo): La cerradura a establecer.
            cual_cerrojo (int): El número de la cerradura en la caverna (1, 2 o 3).

        Returns:
            None
        """
        try:
            if cual_cerrojo+1 == 1:
                self.cerrojo_caverna[0] = puerta
            elif cual_cerrojo+1 == 2:
                self.cerrojo_caverna[1] = puerta
            elif cual_cerrojo+1 == 3:
                self.cerrojo_caverna[2] = puerta
            else:
                print("Índice de gema fuera de rango. La caverna no tiene esa gema.")
                return None
        except IndexError:
            print("Índice de gema fuera de rango. La caverna no tiene esa gema.")
            return None

    def set_letalidad_caverna(self, letalidad, cual_caverna):
        """
        Establece el nivel de letalidad en una caverna específica.

        Args:
            letalidad (float): El nivel de letalidad a establecer.
            cual_caverna (int): El número de la caverna (1, 2 o 3).

        Returns:
            None
        """
        self.letalidad_caverna[cual_caverna - 1] = letalidad

    def get_letalidad_caverna(self, cual_caverna):
        """
        Obtiene el nivel de letalidad en una caverna específica.

        Args:
            cual_caverna (int): El número de la caverna (1, 2 o 3).

        Returns:
            float: El nivel de letalidad en la caverna.
        """
        return self.letalidad_caverna[cual_caverna - 1]

    def __str__(self):
        """
        Obtiene una representación de cadena de la caverna, incluyendo información sobre cerraduras, letalidad y oxígeno.

        Returns:
            str: Una cadena que describe la caverna.
        """
        resumen = ""
        for i in range(3):
            resumen += "--Caverna: " + self.cerrojo_caverna[i].get_nombre_cerrojo() + "--\t"
            resumen += "--Letalidad: " + str(self.letalidad_caverna[i]) + "--\t"
            resumen += "--Oxigeno: " + str(self.oxigeno_caverna[i]) + "--\n\n"
            for j in range(3):
                resumen += "\n" + str(self.cerrojo_caverna[i].get_gema_cerrojo(j))
            resumen += "\n"
        return resumen
