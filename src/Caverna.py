import Cerrojo

class Caverna:
    def __init__(self):
        self.nombre_cerrojo = ["1", "2", "3"]
        self.letalidad_caverna = [0.2, 0.3, 0.4]
        self.cerrojo_caverna = [None] * 3
        self.oxigeno_caverna = [1.0] * 3

        for i in range(3):
            self.cerrojo_caverna[i] = Cerrojo(self.nombre_cerrojo[i])

    def set_oxigeno_jugador_caverna(self, jugador, oxigeno, cual_caverna):
        self.oxigeno_caverna[cual_caverna - 1] = oxigeno
        jugador.set_oxigeno_jugador(self.oxigeno_caverna[cual_caverna - 1])

    def set_oxigeno_caverna(self, cual_caverna, oxigeno):
        self.oxigeno_caverna[cual_caverna - 1] -= oxigeno

    def get_oxigeno_caverna(self, cual_caverna):
        return self.oxigeno_caverna[cual_caverna - 1]

    def get_cerrojo_caverna(self, cual_cerrojo):
        if cual_cerrojo == 1:
            return self.cerrojo_caverna[0]
        elif cual_cerrojo == 2:
            return self.cerrojo_caverna[1]
        else:
            return self.cerrojo_caverna[2]

    def set_cerrojo_caverna(self, puerta, cual_cerrojo):
        if cual_cerrojo == 1:
            self.cerrojo_caverna[0] = puerta
        elif cual_cerrojo == 2:
            self.cerrojo_caverna[1] = puerta
        else:
            self.cerrojo_caverna[2] = puerta

    def set_letalidad_caverna(self, letalidad, cual_caverna):
        self.letalidad_caverna[cual_caverna - 1] = letalidad

    def get_letalidad_caverna(self, cual_caverna):
        return self.letalidad_caverna[cual_caverna - 1]

    def to_string_caverna(self, cual_cerrojo):
        resumen = ""
        resumen += "--Caverna: " + self.cerrojo_caverna[cual_cerrojo - 1].get_nombre_cerrojo() + "--\t"
        resumen += "--Letalidad: " + str(self.letalidad_caverna[cual_cerrojo - 1] * 100.0) + "%--\t"
        resumen += "--Oxigeno:" + str(self.oxigeno_caverna[cual_cerrojo - 1] * 100.0) + "%--\n"
        return resumen

    def __str__(self):
        resumen = ""

        for i in range(3):
            resumen += "--Caverna: " + self.cerrojo_caverna[i].get_nombre_cerrojo() + "--   \t"
            resumen += "  --Letalidad: " + str(self.letalidad_caverna[i]) + "  --\t"
            resumen += "  --Oxigeno: " + str(self.oxigeno_caverna[i]) + "--\n\n\n"
            for j in range(3):
                resumen += "\n" + self.cerrojo_caverna[i].get_gema_cerrojo(j)
            resumen += "\n"
        return resumen