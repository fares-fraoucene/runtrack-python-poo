from Job02 import Livre

class Livremodifié(Livre):
    def __init__(self, titre, auteur, pages):
        super().__init__(titre, auteur, pages)
        self.__disponible = True

    def verif_dispo(self):
        if self.__disponible == True:
            return True
        elif self.__disponible == False:
            return False
        
    def emprunter(self):
        if self.verif_dispo() == True:
                self.__disponible = False
                print("vous avez emprunté le livre")
        else:
             print("Le livre est indisponible")

    def rendre(self):
        if self.verif_dispo() == False:
                self.__disponible = True
                print("vous avez rendu le livre")

n = Livremodifié("naruto", "Kishimoto", 90)

n.emprunter()
n.emprunter()
n.rendre()


    



