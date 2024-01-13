class Personne():
    def __init__(self, nom, prénom):
        self.nom = nom
        self.prénom = prénom
    def SePresente(self):
        print(f"Je suis {self.prénom} {self.nom}")

n = Personne("Jhon","Doe")
y = Personne("Jean","Dupond")
n.SePresente()
y.SePresente()
