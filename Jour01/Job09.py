class Produit():
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
        self.prixTVA = self.CalculerPrixTTC()

    def CalculerPrixTTC(self):
        TVA = self.prixHT * (self.TVA / 100)
        result = self.prixHT + TVA
        return result
    
    def afficher(self):
        return [self.nom,self.prixHT,self.TVA, self.prixTVA]
    def getNom(self):
        return self.nom
    def getPrixHT(self):
        return self.prixHT
    def getTVA(self):
        return self.TVA
    def getPrixTTC(self):
        return self.prixTVA
    
    def setNom(self, nom):
        self.nom = nom
    def setPrixHT(self, prixHT):
        self.prixHT = prixHT
        self.updatePrixTTC()
    def setTVA(self, taux):
        self.TVA = taux
        self.updatePrixTTC()
    def updatePrixTTC(self):
        self.prixTTC = self.CalculerPrixTTC()

coca = Produit("Coca-Cola", 1.50)
print(f"Nom : {coca.getNom()} / ",f"PrixHT : {coca.getPrixHT()}€ / ",f"PrixTTC : {coca.getPrixTTC()}€")

beignet = Produit("Beignet", 2.70)
print(f"Nom : {beignet.getNom()} / ",f"PrixHT : {beignet.getPrixHT()}€ / ",f"PrixTTC : {beignet.getPrixTTC()}€")