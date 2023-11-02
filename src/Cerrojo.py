import random
import Gema

class Cerrojo:
    def __init__(self, nombre="Cerrojo #"):
        """
        Inicializa una instancia de Cerrojo.

        Args:
            nombre (str): El nombre del cerrojo (por defecto, "Cerrojo #").
        """
        self.abierto = False
        self.nombre_cerrojo = nombre
        self.vida_cerrojo = 1.0 * 100
        self.gema_cerrojo = []
        tipo = [self.tipo_aleatorio(), self.tipo_aleatorio(), self.tipo_aleatorio()]
        for i in range(3):
            nueva_gema = Gema.Gema(propietario=self.nombre_cerrojo, tipo=tipo[i],
                        ataque=round(random.uniform(0.6, 1.0) * 100, 2),
                        defensa=round(random.uniform(0.1, 0.5) * 100, 2))
            self.gema_cerrojo.append(nueva_gema)

    def tipo_aleatorio(self):
        """
        Método que genera aleatoriamente un tipo de gema
        (FUEGO, AGUA, METAL).

        Returns:
            str: El tipo de gema generado aleatoriamente.
        """
        valor = random.randint(1, 3)
        if valor == 1:
            return "FUEGO"
        elif valor == 2:
            return "AGUA"
        else:
            return "METAL"

    def set_vida(self, vida):
        """
        Establece el estado de vida del cerrojo.

        Args:
            vida (bool): True si el cerrojo está vivo, False de lo contrario.

        Returns:
            None
        """
        self.vida = vida

    def get_vida(self):
        """
        Obtiene el estado de vida del cerrojo.

        Returns:
            bool: True si el cerrojo está vivo, False de lo contrario.
        """
        return self.vida

    def set_nombre_cerrojo(self, puerta):
        """
        Establece el nombre del cerrojo.

        Args:
            puerta (str): El nombre del cerrojo.

        Returns:
            None
        """
        self.nombre_cerrojo = puerta

    def get_nombre_cerrojo(self):
        """
        Obtiene el nombre del cerrojo.

        Returns:
            str: El nombre del cerrojo.
        """
        return self.nombre_cerrojo

    def set_vida_cerrojo(self, vida):
        """
        Establece el nivel de vida del cerrojo.

        Args:
            vida (float): El nivel de vida del cerrojo (un número entre 0 y 1).

        Returns:
            None
        """
        self.vida_cerrojo = vida

    def get_vida_cerrojo(self):
        """
        Obtiene el nivel de vida del cerrojo.

        Returns:
            float: El nivel de vida del cerrojo (un número entre 0 y 1).
        """
        return self.vida_cerrojo

    def set_vida_gema_cerrojo(self, cual_gema, vida):
        """
        Establece el nivel de vida de una gema en el cerrojo.

        Args:
            cualGema (int): El número de la gema deseada (1, 2 o 3).
            vida (float): El nivel de vida de la gema (un número entre 0 y 1).

        Returns:
            None
        """
        try:
            if cual_gema-1 == 0:
                self.gema_cerrojo[0].set_vida_gema(vida)
            elif cual_gema-1 == 1:
                self.gema_cerrojo[1].set_vida_gema(vida)
            elif cual_gema-1 ==2:
                self.gema_cerrojo[2].set_vida_gema(vida)
            else:
                print("Número de gema no válido. Debe ser 1, 2 o 3.")
                return None
        except IndexError:
            print("Indice de gema fuera de rango. El jugador no tiene esa gema.")
            return None

    def get_gema_cerrojo(self, cual_gema):
        """
        Obtiene una de las gemas del cerrojo por su número (1, 2 o 3).

        Args:
            cualGema (int): El número de la gema deseada (1, 2 o 3).

        Returns:
            Gema: La gema seleccionada.
        """
        try:
            if cual_gema-1 == 0:
                return self.gema_cerrojo[0]
            elif cual_gema-1 == 1:
                return self.gema_cerrojo[1]
            elif cual_gema-1 == 2:
                return self.gema_cerrojo[2]
            else:
                print("Número de gema no válido. Debe ser 1, 2 o 3.")
                return None
        except IndexError:
            print("Indice de gema fuera de rango. El jugador no tiene esa gema.")
            return None

    def __str__(self):
        """
        Obtiene una representación de cadena del cerrojo, incluyendo
        información sobre su nombre, vida y gemas.

        Returns:
            str: Una cadena que describe el cerrojo.
        """
        informacion = "Cerrojo: " + self.nombre_cerrojo + "\n"
        informacion += "Esta abierto el cerrojo? " + ("Si\n" if self.abierto else "No\n")
        informacion += "Porcentaje de vida del cerrojo: " + str(self.vida_cerrojo) + "\n"
        informacion += "Gemas: \n"
        for i in range(3):
            informacion += self.gema_cerrojo[i].__str__() + "\n"
        return informacion
