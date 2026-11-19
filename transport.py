from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def se_deplacer(self):
        print("Les moyens de transports de déplacent")

class Voiture(Transport):
    def se_deplacer(self):
        print("La voiture se déplace sur la route.")

class Avion(Transport):
    def se_deplacer(self):
        print("L'avion vole dans les airs.")

class Bateau(Transport):
    def se_deplacer(self):
        print("Le bateau navigue sur l'eau.")

voiture = Voiture()
avion = Avion()
bateau = Bateau()

transports = [voiture, avion, bateau]

for transport in transports:
    transport.se_deplacer()