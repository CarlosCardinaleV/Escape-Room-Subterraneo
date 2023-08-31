import random

class Gema:
    def __init__(self, tipo="", jugador="", ataque=0.0, defensa=0.0):
        self.tipoGema = tipo
        self.jugadorGema = jugador
        self.vidaGema = 1.0
        self.ataqueGema = ataque
        self.defensaGema = defensa

    def __random_type(self):
        valor = random.randint(1, 3)
        if valor == 1:
            return "FUEGO"
        elif valor == 2:
            return "AGUA"
        else:
            return "METAL"

    def __random_value(self, min_val, max_val):
        return min_val + random.random() * (max_val - min_val)

    def __str__(self):
        informacion = ""
        informacion += "Gema de: " + self.jugadorGema + "\n"
        informacion += "Vida de la Gema: " + str(self.vidaGema * 100.0) + "%\n"
        informacion += "Ataque: " + str(self.ataqueGema) + "\n"
        informacion += "Defensa: " + str(self.defensaGema) + "\n"
        informacion += "El tipo de Gema: " + self.tipoGema + "\n"
        return informacion

    def __str__gema(self):
        return f"{self.tipoGema}:{self.vidaGema * 100.0}%"

    def desplegarGema(self):
        print("Gema de: " + self.jugadorGema)
        print("Vida de la Gema: " + str(self.vidaGema * 100.0) + "%")
        print("Ataque: " + str(self.ataqueGema))
        print("Defensa: " + str(self.defensaGema))
        print("El tipo de Gema: " + self.tipoGema)

    def getTipoGema(self):
        return self.tipoGema

    def getPropietarioGema(self):
        return self.jugadorGema

    def getVidaGema(self):
        return self.vidaGema

    def getAtaqueGema(self):
        return self.ataqueGema

    def getDefensaGema(self):
        return self.defensaGema

    def setTipoGema(self, tipo):
        self.tipoGema = tipo

    def setJugadorGema(self, jugador):
        self.jugadorGema = jugador

    def setVidaGema(self, vida):
        if vida >= 0:
            self.vidaGema = vida
        else:
            self.vidaGema = 0.0

    def setAtaqueGema(self, ataque):
        self.ataqueGema = ataque

    def setDefensaGema(self, defensa):
        self.defensaGema = defensa

    @staticmethod
    def numRandom(min_val, max_val):
        return min_val + random.random() * (max_val - min_val)