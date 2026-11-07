class Formation:
    def __init__(self, intitule, duree):
        self.intitule = intitule
        self.duree = duree

class Etudiant:
    def __init__(self, nom, age, formation):
        self.nom = nom
        self.age = age
        self.formation = formation

    def afficher_informations(self):
        print("nom :", self.nom)
        print("Intitulé de sa formation:",self.formation.intitule)

formation1 = Formation("developpement web", 3)

etudiant1 = Etudiant("Marc", 22, formation1)
etudiant2 = Etudiant("John", 20, formation1)

etudiant1.afficher_informations()
etudiant2.afficher_informations()