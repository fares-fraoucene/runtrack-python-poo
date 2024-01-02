class Personnage():
    def __init__(self):
        self.x = 100
        self.y = 200
    def gauche(self):
        self.x -= 10
    def droite(self):
        self.x += 10
    def bas(self):
        self.y += 10
    def haut(self):
        self.y -= 10
    def position(self):
        return (self.x, self.y)
n = Personnage()

n.bas()
n.droite()
n.bas()
n.droite()
print(n.position())
        
