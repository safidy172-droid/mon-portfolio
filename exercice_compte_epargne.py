class CompteBancaire:
    def __init__(self, nom, solde):
        self.nom = nom
        self.solde = solde
    
    def afficher_solde(self):
        print(f"nom du titulaire: {self.nom} ,le solde disponible: {self.solde}.")

class CompteEpargne(CompteBancaire):
    def __init__(self, nom, solde, interet):
        super().__init__(nom, solde)
        self.interet = interet

    def afficher_solde(self):
        super().afficher_solde()
        print(f" taux d'intérêt: {self.interet} %.")
    
compteepargne1 = CompteEpargne("Miora", 500000, 5)
compteepargne1.afficher_solde()   
