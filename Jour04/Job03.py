class Rectangle():
    def __init__(self, longueur,largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    def perimètre(self):
        perimetre = 2 * (self.__longueur + self.__largeur)
        return print(f"Le Périmetre est de {perimetre} cm")
    def surface(self):
        surface = self.__longueur * self.__largeur
        return print(f"La surface du Rectangle est :{surface} cm")
    def get_longueur(self):
        return self.__longueur
    def get_largeur(self):
        return self.__largeur
    def modifier_largeur(self, new_value):
        self.__largeur = new_value
    def modifier_longueur(self, new_value):
        self.__longueur = new_value

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        air = self.get_longueur() * self.get_largeur()
        volume = air * self.__hauteur
        return print(f"Le volume du Parallelepipede est :{volume} cm")
n = Rectangle(20,20)
y = Parallelepipede(15,15,20)
n.perimètre()
n.surface()
y.perimètre()
y.surface()
y.volume()