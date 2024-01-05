class Personne:
    def __init__(self):
        self.age = 14
    def afficherAge(self):
        return print(f"Age : {self.age} ans")
    def bonjour():
        return print("Hello")
    def modifierAge(self,new_age):
        self.age = new_age

class Eleve(Personne):
    def __init__(self):
        Personne.__init__(self)
    def allerEnCours(self):
        return print("Je vais en cours")

class Professeur(Personne):
    def __init__(self):
        self.__matiereEnseignée = "Anglais"
        Personne.__init__(self)
    def enseigner(self):
        return print(f"Le cours d'{self.__matiereEnseignée} va commencer")
    

y = Eleve()
n = Professeur()
y.afficherAge()
n.modifierAge(35)
n.afficherAge()
y.allerEnCours()
n.enseigner()
