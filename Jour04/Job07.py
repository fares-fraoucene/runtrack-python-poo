import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = self.initialiser_paquet()

    def initialiser_paquet(self):
        valeurs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # Les valeurs possibles pour chaque carte
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']  # Les couleurs des cartes
        paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        random.shuffle(paquet)
        return paquet

    def calculer_points(self, main):
        points = sum(carte.valeur for carte in main)
        as_count = sum(1 for carte in main if carte.valeur == 11)

        while points > 21 and as_count:
            points -= 10
            as_count -= 1

        return points

    def afficher_main(self, main):
        for carte in main:
            print(f"{carte.valeur} de {carte.couleur}")

    def jouer_partie(self):
        main_joueur = [self.paquet.pop(), self.paquet.pop()]  # Distribuer 2 cartes au joueur
        main_croupier = [self.paquet.pop(), self.paquet.pop()]  # Distribuer 2 cartes au croupier

        while True:
            print("\nMain du joueur:")
            self.afficher_main(main_joueur)
            points_joueur = self.calculer_points(main_joueur)
            print(f"Total des points du joueur : {points_joueur}")

            if points_joueur == 21:
                print("Blackjack ! Le joueur gagne.")
                return

            action = input("Voulez-vous prendre une carte (p) ou passer (n) ? ").lower()

            if action == 'p':
                main_joueur.append(self.paquet.pop())
                if self.calculer_points(main_joueur) > 21:
                    print("Vous avez dépassé 21. Le croupier gagne.")
                    return
            elif action == 'n':
                break

        while self.calculer_points(main_croupier) < 17:
            main_croupier.append(self.paquet.pop())

        print("\nMain du croupier:")
        self.afficher_main(main_croupier)
        points_croupier = self.calculer_points(main_croupier)
        print(f"Total des points du croupier : {points_croupier}")

        if points_croupier > 21 or points_joueur > points_croupier:
            print("Le joueur gagne!")
        elif points_joueur == points_croupier:
            print("Égalité!")
        else:
            print("Le croupier gagne!")

if __name__ == "__main__":
    jeu = Jeu()
    jeu.jouer_partie()
