class Vehicule:
    def __init__(self, marque,modele,année,prix):
        self.__marque = marque
        self.__modele = modele
        self.__année = année
        self.__prix = prix
    def get_marque(self):
        return self.__marque
    def get_modele(self):
        return self.__modele
    def get_année(self):
        return self.__année
    def get_prix(self):
        return self.__prix
    def informationsVehicule(self):
        return print(f"Marque = {self.get_marque()} \nModele = {self.get_modele()} \nAnnée = {self.get_année()} \nPrix = {self.get_prix()} €")
class Voiture(Vehicule):
    def __init__(self, marque, modele, année, prix):
        super().__init__(marque, modele, année, prix)
        self.__porte = 4
    def get_nombre_portes(self):
        return self.__porte
    def informationsVehicule(self):
        return print(f"Marque = {self.get_marque()} \nModele = {self.get_modele()} \nAnnée = {self.get_année()} \nPrix = {self.get_prix()} € \nNombre de porte = {self.get_nombre_portes()}")

class Moto(Vehicule):
    def __init__(self, marque, modele, année, prix):
        super().__init__(marque, modele, année, prix)
        self.__roue = 2
    def get_nombre_roue(self):
        return self.__roue
    def informationsVehicule(self):
        return print(f"Marque = {self.get_marque()} \nModele = {self.get_modele()} \nAnnée = {self.get_année()} \nPrix = {self.get_prix()} € \nNombre de roue = {self.get_nombre_roue()}")
    
n=Voiture("Mercedes","Classe A",2020,18500)
y=Moto("Yamaha", "1200 Vmax", 1987, 4500)
n.informationsVehicule()
y.informationsVehicule()

