class Personne():
    def __init__(self):
        self.nom = ["Doe", "Dupond"]
        self.prénom = ["Jhon", "Jean"]
    def SePresente(self):
        print(f"Je suis {self.prénom[0]} {self.nom[0]}")
        print(f"Je suis {self.prénom[1]} {self.nom[1]}")

n = Personne()
n.SePresente()
