class Morpion:
    def __init__(self, taille=3):
        self.taille = taille
        self.grille = [[' ' for _ in range(taille)] for _ in range(taille)]
        self.joueur_actuel = 'X'
        self.adversaire = 'O'

    def afficher_grille(self):
        level = [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"],
        ]
        for ligne in level:
            print(' | '.join(ligne))
            print('-' * (4 * self.taille - 1))

    def poser_pion(self, ligne, colonne):
        if self.grille[ligne][colonne] == ' ':
            self.grille[ligne][colonne] = self.joueur_actuel
            return True
        else:
            print("Cet emplacement est déjà occupé. Essayez à nouveau.")
            return False

    def verifier_ligne(self):
        for ligne in self.grille:
            if all(pion == self.joueur_actuel for pion in ligne):
                return True
        return False

    def verifier_colonne(self):
        for col in range(self.taille):
            if all(self.grille[ligne][col] == self.joueur_actuel for ligne in range(self.taille)):
                return True
        return False

    def verifier_diagonale(self):
        if all(self.grille[i][i] == self.joueur_actuel for i in range(self.taille)) or \
           all(self.grille[i][self.taille - 1 - i] == self.joueur_actuel for i in range(self.taille)):
            return True
        return False

    def tour_par_tour(self):
        self.joueur_actuel, self.adversaire = self.adversaire, self.joueur_actuel

    def ennemi_intelligent(self):
        # Implémentez ici la logique pour que l'adversaire pose un pion intelligemment.
        # Vous pouvez utiliser des stratégies simples comme bloquer les lignes/colonnes/diagonales de l'adversaire.
        pass  # Remplacez cette ligne par votre propre code

    def verifier_victoire(self):
        if self.verifier_ligne() or self.verifier_colonne() or self.verifier_diagonale():
            return True
        return False

    def recommencer(self):
        choix = input("Voulez-vous recommencer ? (O/N) ").upper()
        return choix == 'O'

    def jouer(self):
        while True:
            self.afficher_grille()
            ligne = int(input("Entrez le numéro de ligne (0 à {}): ".format(self.taille - 1)))
            colonne = int(input("Entrez le numéro de colonne (0 à {}): ".format(self.taille - 1)))

            if self.poser_pion(ligne, colonne):
                if self.verifier_victoire():
                    print(f"Le joueur {self.joueur_actuel} a gagné !")
                    if not self.recommencer():
                        break
                self.tour_par_tour()

if __name__ == "__main__":
    jeu = Morpion()
    jeu.jouer()
