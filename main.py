class Moteur:
    def __init__(self, marque, puissance):
        self.marque = marque
        self.puissance = puissance

    def demarrer(self):
        print("Le moteur demarre !")

class Voiture(Moteur):
    def __init__(self, marque, puissance):
        self.moteur = Moteur(marque, puissance)

    def demarrer(self):
        self.moteur.demarrer()
          

voiture = Voiture("BMW", 250)
voiture.demarrer()