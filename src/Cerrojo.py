import Gema

class Cerrojo:
    def __init__(self, nombre="Cerrojo #"):
        """
        Inicializa una instancia de Cerrojo.

        Args:
            nombre (str): El nombre del cerrojo (por defecto, "Cerrojo #").
        """
        self.vida = True
        self.nombreCerrojo = nombre
        self.vidaCerrojo = 1.0
        self.gemaCerrojo = [Gema() for _ in range(3)]

    def setVida(self, vida):
        """
        Establece el estado de vida del cerrojo.

        Args:
            vida (bool): True si el cerrojo está vivo, False de lo contrario.

        Returns:
            None
        """
        self.vida = vida

    def getVida(self):
        """
        Obtiene el estado de vida del cerrojo.

        Returns:
            bool: True si el cerrojo está vivo, False de lo contrario.
        """
        return self.vida

    def setNombreCerrojo(self, puerta):
        """
        Establece el nombre del cerrojo.

        Args:
            puerta (str): El nombre del cerrojo.

        Returns:
            None
        """
        self.nombreCerrojo = puerta

    def getNombreCerrojo(self):
        """
        Obtiene el nombre del cerrojo.

        Returns:
            str: El nombre del cerrojo.
        """
        return self.nombreCerrojo

    def setVidaCerrojo(self, vida):
        """
        Establece el nivel de vida del cerrojo.

        Args:
            vida (float): El nivel de vida del cerrojo (un número entre 0 y 1).

        Returns:
            None
        """
        self.vidaCerrojo = vida

    def getVidaCerrojo(self):
        """
        Obtiene el nivel de vida del cerrojo.

        Returns:
            float: El nivel de vida del cerrojo (un número entre 0 y 1).
        """
        return self.vidaCerrojo

    def setVidaGemaCerrojo(self, cualGema, vida):
        """
        Establece el nivel de vida de una gema en el cerrojo.

        Args:
            cualGema (int): El número de la gema deseada (1, 2 o 3).
            vida (float): El nivel de vida de la gema (un número entre 0 y 1).

        Returns:
            None
        """
        if cualGema == 1:
            self.gemaCerrojo[0].setVidaGema(vida)
        elif cualGema == 2:
            self.gemaCerrojo[1].setVidaGema(vida)
        else:
            self.gemaCerrojo[2].setVidaGema(vida)

    def getGemaCerrojo(self, cualGema):
        """
        Obtiene una de las gemas del cerrojo por su número (1, 2 o 3).

        Args:
            cualGema (int): El número de la gema deseada (1, 2 o 3).

        Returns:
            Gema: La gema seleccionada.
        """
        if cualGema == 1:
            return self.gemaCerrojo[0]
        elif cualGema == 2:
            return self.gemaCerrojo[1]
        else:
            return self.gemaCerrojo[2]

    def __str__(self):
        """
        Obtiene una representación de cadena del cerrojo, incluyendo
        información sobre su nombre, vida y gemas.

        Returns:
            str: Una cadena que describe el cerrojo.
        """
        informacion = "Caverna: " + self.nombreCerrojo + "\n"
        informacion += "Porcentaje de vida de la Caverna: " + str(self.vidaCerrojo) + "\n"
        informacion += "Gemas: \n"
        for i in range(3):
            informacion += self.gemaCerrojo[i].__str__() + "\n"
        return informacion

    def toStringCerrojo(self):
        """
        Obtiene una representación de cadena del cerrojo, incluyendo
        información sobre su nombre, vida y estado de las gemas.

        Returns:
            str: Una cadena que describe el cerrojo.
        """
        informacion = "Caverna: " + self.nombreCerrojo + "\n"
        informacion += "Gemas: \n"
        informacion += "Primera Gema: " + str(self.gemaCerrojo[0].getVidaGema()) + "%  "
        informacion += "Segunda Gema: " + str(self.gemaCerrojo[1].getVidaGema()) + "%  "
        informacion += "Tercera Gema: " + str(self.gemaCerrojo[2].getVidaGema()) + "%  \n"
        return informacion

    def desplegarCerrojo(self):
        """
        Imprime información sobre el cerrojo, incluyendo el nombre,
        nivel de vida y estado de las gemas.

        Returns:
            None
        """
        print("Nivel: " + self.nombreCerrojo)
        print("Porcentaje de vida de la Caverna: " + str(self.vidaCerrojo))
        print("Gemas: ")
        for i in range(3):
            print(self.gemaCerrojo[i].__str__())
