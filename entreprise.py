from abc import ABC, abstractmethod

class Employe(ABC):
    def __init__(self, nom, salaire):
        self.nom = nom
        self.salaire = salaire

    def calculer_salaire(self):
        return self.salaire

class Developpeur(Employe):
    def __init__(self, nom, salaire,prime_technique):
        super().__init__(nom, salaire)
        self.prime_technique = prime_technique

    def calculer_salaire(self):
        return self.salaire + self.prime_technique

class Commercial(Employe):
    def __init__(self, nom, salaire, commission):
        super().__init__(nom, salaire)
        self.commission = commission

    def calculer_salaire(self):
        return self.salaire + self.commission

developpeur1 = Developpeur("Soa",1000000,500000)
developpeur2 = Developpeur("Maxime",1000000, 750000)
commercial1 = Commercial("skyler", 1000000, 800000)
commercial2 = Commercial("Sonia", 1000000, 900000)

employers = [developpeur1, developpeur2, commercial1, commercial2]

for employer in employers:
    print("Employé:",employer.nom,)
    print( "Salaire = ", employer.calculer_salaire())