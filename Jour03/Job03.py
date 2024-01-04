class Tache:
    def __init__(self, titre, description, statut):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"{self.titre} - {self.description} - {self.statut}"

    def set_statut(self, nouveau_statut):
        self.statut = nouveau_statut

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimer_tache(self, tache):
        self.taches.remove(tache)

    def marquerCommeFinie(self, tache):
        tache.set_statut("Finie")

    def afficherListe(self):
        for tache in self.taches:
            print(tache)

    def filterListe(self, statut):
        taches_filtrees = []
        for tache in self.taches:
            if tache.statut == statut:
                taches_filtrees.append(tache)
        return taches_filtrees

n = Tache("Pc", "Finir Jour03", "Faire")
x = Tache("Pc", "Finir Jour02", "Faire")
y = ListeDeTaches()
y.ajouterTache(n)
y.ajouterTache(x)
y.marquerCommeFinie(x)
print("Liste après modification:")
y.afficherListe()
v = y.filterListe("Faire")
print("Tâches à faire:")
for tache in v:
    print(tache)
