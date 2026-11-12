class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee

    def afficher_details(self):
        print("titre du livre:",self.titre)
        print("Ecrit par:",self.auteur)
        print(" Paru en:",self.annee)

class Bibliotheque:
    def __init__(self):
        self.livres = [] 

    def ajouter_livre(self, livre):
        self.livres.append(livre)
      

    def afficher_catalogue(self):
       for livre in self.livres:
        livre.afficher_details()

           
livre1 = Livre("Le Petit Prince","Antoine de Saint-Exupéry",1943 )         
livre2 = Livre("Miguel de Cervantes","Mao Zedong", 1964)
livre3 = Livre("Un conte de deux villes","Charles Dickens",1859)


bibliotheque = Bibliotheque()
bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)
bibliotheque.ajouter_livre(livre3)

bibliotheque.afficher_catalogue()
