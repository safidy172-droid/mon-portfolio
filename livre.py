class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee

    def afficher_details(self):
        print("titre du livre:",self.titre)
        print("Ecrit par:",self.auteur)
        print("en",self.annee)

class Bibliotheque:
    def __init__(self, liste):
        self.liste = liste 

    def ajouter_livre(self):
        
      

    def afficher_catalogue(self):
       for livre in livres:
        livres.afficher_details()

           
livre1 = Livre("Miguel de Cervantes","Miguel de Cervantes",1605 )         
livre2 = Livre("Miguel de Cervantes","Mao Zedong", 1964)
livre3 = Livre("Un conte de deux villes","Charles Dickens",1859)
livres = [livre1, livre2, livre3]

bibliotheque = Bibliotheque()
bibliotheque.ajouter_livre(livres)

