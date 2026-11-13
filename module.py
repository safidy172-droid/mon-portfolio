
class Apprenant:
    def __init__(self, nom, identifiant,liste):
        self.nom = nom
        self.identifiant = identifiant
        self.list = liste
        self.modules = []
        
    def inscrire(self,module):
        self.modules.append(module)
    
    def afficher_modules(self):
       
        for module in self.modules:
            print(f" nom: {self.nom} , id:{self.identifiant} ,{module.titre} : {module.heure} heures")
            
class Module:
    def __init__(self, titre, heure):
        self.titre = titre
        self.heure = heure

    
apprenant1 = Apprenant("Lucas","0100-AAA",2)
apprenant2 = Apprenant("Martin","0111-BBB",4)

module1 = Module("HTML",12)
module2 = Module("JavaScript",48)
module3 = Module("POO",64)

apprenant1.inscrire(module1)
apprenant1.inscrire(module3)
apprenant2.inscrire(module2)
apprenant2.inscrire(module1)

apprenant1.afficher_modules()
apprenant2.afficher_modules()