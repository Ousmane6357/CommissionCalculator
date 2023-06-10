class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("Pío")

    def volar(self,metros):
        print(f"El pajaro ha volado {metros} metros" )
        self.piar()


    def pinta_negro(self):
        self.color ='Negro'
        print(f"Ahora es pajaro es {self.color} ")

    @classmethod
    def poner_huevos(cls,cantidad):
        print(f"Puso {cantidad} huevos ")
        cls.alas = False
        print(Pajaro.alas)

    @staticmethod
    def mirar():
        print("El pajaro bigila")


Pajaro.mirar()
