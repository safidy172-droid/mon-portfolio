class Module:
    def __init__(self, titre,duree):
        self.titre = titre
        self.duree = duree

class Formation:
    def __init__(self, intitule, liste):
        self.intitule = intitule
        self.liste = liste
        self.modules = []
    
    def ajouter_module(self, module):
        self.modules.append(module)        

class Apprenant:
    def __init__(self, nom):
        self.nom = nom
        self.liste_formation = []
    
    def s_inscrire(self, formation):
        self.liste_formation.append(formation)
        

    def afficher_parcours(self):
       print(f"Nom Apprenant : {self.nom}")
       
       for formation in self.liste_formation: 
         print(f"intitule de formation : {formation.intitule} .")
         
         for module in formation.modules:
             print(f"Nom module: {module.titre}")
             print(f"Durée : {module.duree} heures")

module1 = Module("POO", 48)
module2 = Module("JavaScript", 64)

formation1 = Formation("full stack 1","HTML5")
formation2 = Formation("full stack 2","Node.Js")

formation1.ajouter_module(module1)
formation2.ajouter_module(module2)

apprenant1 = Apprenant("Jack",)
apprenant2 = Apprenant("Paul")

apprenant1.s_inscrire(formation1)
apprenant2.s_inscrire(formation2)

apprenant1.afficher_parcours()
apprenant2.afficher_parcours()