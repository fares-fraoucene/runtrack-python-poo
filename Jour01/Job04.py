class Personne():
    nom = ["Doe", "Dupond"]
    prénom = ["Jhon", "Jean"]
    def SePresente(self):
        print(f"Je suis {self.prénom[0]} {self.nom[0]}")
        print(f"Je suis {self.prénom[1]} {self.nom[1]}")

n = Personne()
n.SePresente()
