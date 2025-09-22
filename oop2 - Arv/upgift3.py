class Person:
    def __init__(self, namn, personnummer):
        self.namn = namn
        self.personnummer = personnummer
    def beskrivning(self):
        print(f"{self.namn} | {self.personnummer}")

class Anställd(Person):
    def __init__(self, namn, personnummer, anställningsnummer):
        super().__init__(namn, personnummer)
        self.anstälnningsnummer = anställningsnummer
    def beskrivning(self):
        print(f"{self.namn} | {self.personnummer} är anställd med anställningsnummer {self.anstälnningsnummer}")

class Lärare(Anställd):
    def __init__(self, namn, personnummer, anställningsnummer, ämne):
        super().__init__(namn, personnummer, anställningsnummer)
        self.ämne = ämne
    def beskrivning(self):
        print(f"{self.namn} | {self.personnummer} är lärare med anställningsnummer {self.anstälnningsnummer} och undervisar i {self.ämne}")

class Rektor(Anställd):
    def __init__(self, namn, personnummer, anställningsnummer, ansvarsområde):
        super().__init__(namn, personnummer, anställningsnummer)
        self.ansvarsområde = ansvarsområde
    def beskrivning(self):
        print(f"{self.namn} | {self.personnummer} är rektor med anställningsnummer {self.anstälnningsnummer} och ansvarar för {self.ansvarsområde}")

person_lista = []

person_lista.append()