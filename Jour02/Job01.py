class Rectancle():
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    def change_largeur(self,new_largeur):
        self.__largeur = new_largeur
    def change_longueur(self,new_longueur):
        self.__longueur = new_longueur
    def afficherInfos(self):
        return(self.__longueur,self.__largeur)
n = Rectancle(10,5)
print(n.afficherInfos())
n.change_longueur(20)
n.change_largeur(10)
print(n.afficherInfos())


        