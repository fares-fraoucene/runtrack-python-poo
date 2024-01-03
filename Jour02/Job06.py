class Commande():
    def __init__(self):
        self.__numéro_de_commande = int()
        self.__liste_plat_commandé = list(str())
        self.__statues_commande = str()
        self.__prix = 0
    def ajouter_plat(self, new_plat):
        if new_plat == str(new_plat):
            self.__liste_plat_commandé.append(new_plat)
        else:
            print("Ce n'est pas du texte")
        return self.__liste_plat_commandé
    def get_liste_plat_commandé(self):
        return self.__liste_plat_commandé
    def annuler_une_commande(self):
        self.__statues_commande = "Annuler"
    def get_statue_commande(self):
        return self.__statues_commande
    def calculer_total(self):
        



    

n = Commande()
n.ajouter_plat(25)
n.ajouter_plat("Pizza")
n.ajouter_plat("Tiramusu")
print(n.get_liste_plat_commandé())
n.annuler_une_commande()
print(n.get_statue_commande())


        