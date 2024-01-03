class Livre():
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
    def change_auteur(self, new_auteur):
        self.__auteur = new_auteur
    def change_titre(self, new_titre):
        self.__titre = new_titre
    def change_page(self, new_pages):
        if isinstance(new_pages,int) and new_pages >= 0:
            self.__pages = new_pages
        else: 
            print("ce chiffre doit etre un entier positif")

    def afficher_auteur(self):
        print(self.__auteur)
        return self.__auteur
    def afficher_titre(self):
        print(self.__titre)
        return self.__titre
    def afficher_pages(self):
        print(self.__pages)
        return self.__pages
n = Livre("one piece", "Oda", 80)
n.afficher_titre()
n.afficher_auteur()
n.afficher_pages()
n.change_page(-10)
n.change_page("Salut")
n.change_page(10)
n.afficher_pages()


    




        