class Opération():
    nombre1 = 12
    nombre2 = 3
    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(f"Résultat de l'addition {resultat}")
n = Opération()

n.addition()