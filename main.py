
class Employe:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        print(f"Je m'appelle {self.nom} et j'ai {self.age} ans.")

class Developpeur(Employe):
    def __init__(self, nom, age, language):
        super().__init__(nom, age)
        self.language = language

    def se_presenter(self):
        super().se_presenter()
        print(f"Ma language de programmation préféré est {self.language} .")

developpeur1 = Developpeur("Soa", 25, "python")
developpeur1.se_presenter()