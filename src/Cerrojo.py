import random
import Gema

class Cerrojo:
    def __init__(self, nombre="Cerrojo #"):
        """
        Inicializa una instancia de Cerrojo.

        Args:
            nombre (str): El nombre del cerrojo (por defecto, "Cerrojo #").
        """
        self.__abierto_cerrojo = False
        self.__nombre_cerrojo = nombre
        self.__vida_cerrojo = 1.0 * 100
        self.__gema_cerrojo = []
        tipo = [self.tipo_aleatorio(), self.tipo_aleatorio(), self.tipo_aleatorio()]
        for i in range(3):
            nueva_gema = Gema.Gema(propietario=self.__nombre_cerrojo, tipo=tipo[i],
                        ataque=round(random.uniform(0.6, 1.0) * 100, 2),
                        defensa=round(random.uniform(0.1, 0.5) * 100, 2))
            self.__gema_cerrojo.append(nueva_gema)

    @property
    def abierto_cerrojo(self):
        """
        Obtiene respuesta si el cerrojo esta abierto o cerrado.

        Returns:
            bool: True si el cerrojo está abierto, False de lo contrario.
        """
        return self.__abierto_cerrojo
    
    @abierto_cerrojo.setter
    def abierto_cerrojo(self, abierto):
        """
        Establece si el cerrojo esta abierto o cerrado.

        Args:
            abierto (bool): True si el cerrojo está abierto, False de lo contrario.

        Returns:
            None
        """
        self.__abierto_cerrojo = abierto


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

    @property
    def vida_cerrojo(self):
        """
        Obtiene el estado de vida del cerrojo.

        Returns:
            bool: True si el cerrojo está vivo, False de lo contrario.
        """
        return self.__vida_cerrojo

    @vida_cerrojo.setter
    def vida_cerrojo(self, vida):
        """
        Establece el estado de vida del cerrojo.

        Args:
            vida (bool): True si el cerrojo está vivo, False de lo contrario.

        Returns:
            None
        """
        self.__vida_cerrojo = vida

    @property
    def nombre_cerrojo(self):
        """
        Obtiene el nombre del cerrojo.

        Returns:
            str: El nombre del cerrojo.
        """
        return self.__nombre_cerrojo

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
                return self.__gema_cerrojo[0]
            elif cual_gema-1 == 1:
                return self.__gema_cerrojo[1]
            elif cual_gema-1 == 2:
                return self.__gema_cerrojo[2]
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
        informacion = "Cerrojo: " + self.__nombre_cerrojo + "\n"
        informacion += "Esta abierto el cerrojo? " + ("Si\n" if self.__abierto_cerrojo else "No\n")
        informacion += "Porcentaje de vida del cerrojo: " + str(self.__vida_cerrojo) + "\n"
        informacion += "Gemas: \n"
        for i in range(3):
            informacion += self.__gema_cerrojo[i].__str__() + "\n"
        return informacion
