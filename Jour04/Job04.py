class Forme:
    
    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def getLongueur(self):
        return self.__longueur
    def getLargeur(self):
        return self.__largeur
    
    def setLongueur(self, new_val):
        self.__longueur = new_val
    def setLargeur(self, new_val):
        self.__largeur =new_val
        
    def aire(self):
        return print("l'air est de ",self.getLongueur() * self.getLargeur(),"cm")
n = Rectangle(20, 45)
n.aire()
