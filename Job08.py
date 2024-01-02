import math
class Cercle():
    def __init__(self) -> None:
        self.rayon1 = 4
        self.rayon2 = 7
    def changerRayonCercle1(self, new_value):
        self.rayon1 = new_value
    def changerRayonCercle2(self, new_value):
        self.rayon2 = new_value
    def circonference1(self):
        circonference1 = 2 * math.pi * self.rayon1
        return circonference1
    def circonference2(self):
        circonference2 = 2 * math.pi * self.rayon2
        return circonference2
    def air1(self):
        air1 = math.pi * (self.rayon1**2)
        return air1
    def air2(self):
        air2 = math.pi * (self.rayon2**2)
        return air2
    def diametre1(self):
        diametre1 = self.rayon1 * 2
        return diametre1
    def diametre2(self):
        diametre2 = self.rayon2 * 2
        return diametre2
    def afficherInfos1(self):
        print(f"Info du cercle 2(rayon de {self.rayon1}) :")
        print("Circonference: ", self.circonference1())
        print("Aire: ", self.air1())
        print("Diametre: ", self.diametre1())
    def afficherInfos2(self):
        print(f"Info du cercle 2(rayon de {self.rayon2}) :")
        print("Circonference: ", self.circonference2())
        print("Aire: ", self.air2())
        print("Diametre: ", self.diametre2())   

n = Cercle()

n.afficherInfos1()
n.afficherInfos2()
n.changerRayonCercle1(10)
n.changerRayonCercle2(20)
n.afficherInfos1()
n.afficherInfos2()