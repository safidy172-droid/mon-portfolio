class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

class Commande:
    def __init__(self,produit, quantite):
        self.produit = produit
        self.quantite = quantite

    def calculer_total(self):
        return self.produit.prix * self.quantite
    
    def afficher_commande(self):
        print("Nom du produit:", self.produit.nom )
        print("Quantité:", self.quantite )
        print("Montant total:", self.calculer_total(), "Ar")

    
produit1 = Produit("stylo", 1000)
Commande1 = Commande(produit1, 4)
Commande1.afficher_commande()
