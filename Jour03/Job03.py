class Tache():
    def __init__(self,titre,description,):
        self.__titre = titre
        self.__description = description
        self.__statut = ["A faire", "Terminer"]
    def get_titre(self):
        return self.__titre
    def get_descrpition(self):
        return self.__description
    def get_statue(self):
        return self.__statut

n = Tache("ù","é",)




