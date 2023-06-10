class Vaca:


    def __init__(self,nombre):
        self.nombre = nombre


    def hablar(self):
        print(self.nombre + " Muu")


class Oveja:
    def __init__(self,nombre):
        self.nombre = nombre


    def hablar(self):
        print(self.nombre + " M'beee")


vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')

animales = [vaca1,oveja1]

def animal_hablar(animal):
    animal.hablar()

animal_hablar(oveja1)

