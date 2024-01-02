class Animal():
    def __init__(self):
        self.age = 0
        self.prénom = "Nobara"
    def vieillir(self):
        self.age += 1
        print(f"L'age de l'animal est {self.age}")
    def nommer(self, new_name):
        self.name = new_name
        print(f"L'animal se nomme {self.name}")
        

n = Animal()
n.vieillir()
n.nommer("Megumi")

