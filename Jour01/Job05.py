class Point():
    def __init__(self):
        self.x = 100
        self.y = 100
    def afficherLesPoints(self):
        print(f"x = {self.x} et y = {self.y}")
    def afficherX(self):
        print(f"x = {self.x}")
    def afficherY(self):
        print(f"y = {self.y}")  
    def changerX(self, new_x):
        self.x = new_x
    def changerY(self, new_y):
        self.y = new_y
n = Point()
n.afficherLesPoints()
n.afficherX()
n.afficherY()
n.changerX(200)
n.changerY(200)
n.afficherLesPoints()



    