class Joueur:
    def __init__(self, nom, numero, position):
        self.__nom = nom
        self.__numero = numero
        self.__position = position
        self.__buts_marques = 0
        self.__passes_decisives = 0
        self.__cartons_jaunes = 0
        self.__cartons_rouges = 0
    def marquerBut(self):
        self.__buts_marques += 1
    def effectuerUnePasseDecisive(self):
        self.__passes_decisives += 1
    def recevoirUnCartonJaune(self):
        self.__cartons_jaunes += 1
    def recevoirUnCartonRouge(self):
        self.__cartons_rouges += 1
    def afficherStatistiques(self):
        print(f"Nom : {self.__nom} - Numéro : {self.__numero} - Position : {self.__position} - Buts marqués : {self.__buts_marques} - Passes décisives : {self.__passes_decisives} - Cartons rouges : {self.__cartons_rouges}")
class Equipe:
    def __init__(self, nom_equipe):
        self.__nom_equipe = nom_equipe
        self.__liste_joueurs = []
    def ajouter_joueur(self, joueur):
        self.__liste_joueurs.append(joueur)
    def AfficherStatistiquesJoueurs(self):
        for joueur in self.__liste_joueurs:
            joueur.afficherStatistiques()
    def mettreAJourStatistiquesJoueur(self, numero_joueur, action):
        for joueur in self.__liste_joueurs:
            if joueur._Joueur__numero == numero_joueur:  
                if action == "But":
                    joueur.marquerBut()
                elif action == "Passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "Carton jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "Carton rouge":
                    joueur.recevoirUnCartonRouge()
n = Joueur("Fares", 15, "Attaquant")
y = Joueur("Edine", 5, "Attaquant")
x = Joueur("Tansel", 10, "Attaquant")
v = Equipe("Marseille")
v.ajouter_joueur(n)
v.ajouter_joueur(y)
v.ajouter_joueur(x)
v.AfficherStatistiquesJoueurs()
v.mettreAJourStatistiquesJoueur(15, "But")
v.mettreAJourStatistiquesJoueur(5, "Passe")
v.mettreAJourStatistiquesJoueur(10, "Carton jaune")
v.mettreAJourStatistiquesJoueur(10, "Carton rouge")
v.AfficherStatistiquesJoueurs()
