import math
class Cercle():
    def __init__(self, rayon):
        self.rayon = rayon
    def changerRayonCercle(self, new_value):
        self.rayon = new_value
    def circonference(self):
        circonference1 = 2 * math.pi * self.rayon
        return circonference1
    def air(self):
        air1 = math.pi * (self.rayon**2)
        return air1
    def diametre(self):
        diametre1 = self.rayon * 2
        return diametre1
    def afficherInfos(self):
        print(f"Info du cercle 2(rayon de {self.rayon}) :")
        print("Circonference: ", self.circonference())
        print("Aire: ", self.air())
        print("Diametre: ", self.diametre())
  

n = Cercle(4)
n.afficherInfos()
n.changerRayonCercle(7)
n.afficherInfos()