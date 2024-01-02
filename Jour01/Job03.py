class Opération():
    def __init__(self):
        self.nombre1 = 1
        self.nombre2 = 2
    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(f"Résultat de l'addition {resultat}")
n = Opération()

n.addition()