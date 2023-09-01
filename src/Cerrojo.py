import Gema

class Cerrojo:
    def __init__(self, nombre="Cerrojo #"):
        self.vida = True
        self.nombreCerrojo = nombre
        self.vidaCerrojo = 1.0
        self.gemaCerrojo = [Gema() for _ in range(3)]

    def setVida(self, vida):
        self.vida = vida

    def getVida(self):
        return self.vida

    def setNombreCerrojo(self, puerta):
        self.nombreCerrojo = puerta

    def getNombreCerrojo(self):
        return self.nombreCerrojo

    def setVidaCerrojo(self, vida):
        self.vidaCerrojo = vida

    def getVidaCerrojo(self):
        return self.vidaCerrojo

    def setVidaGemaCerrojo(self, cualGema, vida):
        if cualGema == 1:
            self.gemaCerrojo[0].setVidaGema(vida)
        elif cualGema == 2:
            self.gemaCerrojo[1].setVidaGema(vida)
        else:
            self.gemaCerrojo[2].setVidaGema(vida)

    def getGemaCerrojo(self, cualGema):
        if cualGema == 1:
            return self.gemaCerrojo[0]
        elif cualGema == 2:
            return self.gemaCerrojo[1]
        else:
            return self.gemaCerrojo[2]

    def __str__(self):
        informacion = "Caverna: " + self.nombreCerrojo + "\n"
        informacion += "Porcentaje de vida de la Caverna: " + str(self.vidaCerrojo) + "\n"
        informacion += "Gemas: \n"
        for i in range(3):
            informacion += self.gemaCerrojo[i].__str__() + "\n"
        return informacion

    def toStringCerrojo(self):
        informacion = "Caverna: " + self.nombreCerrojo + "\n"
        informacion += "Gemas: \n"
        informacion += "Primera Gema: " + str(self.gemaCerrojo[0].getVidaGema()) + "%  "
        informacion += "Segunda Gema: " + str(self.gemaCerrojo[1].getVidaGema()) + "%  "
        informacion += "Tercera Gema: " + str(self.gemaCerrojo[2].getVidaGema()) + "%  \n"
        return informacion

    def desplegarCerrojo(self):
        print("Nivel: " + self.nombreCerrojo)
        print("Porcentaje de vida de la Caverna: " + str(self.vidaCerrojo))
        print("Gemas: ")
        for i in range(3):
            print(self.gemaCerrojo[i].__str__())
