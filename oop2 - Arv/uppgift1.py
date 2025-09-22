class Djur:
    def __init__(self, namn, födelseÅr):
        self.namn = namn
        self.födelseÅr = födelseÅr

    def ljud():
        print(f"Djur läte")
    def beskrivning(self):
        print(f"{self.namn} är född år {self.födelseÅr} ")
    def mata(self):
        print(f"{self.namn} har blivit matad")
    def lek(self):
        print(f"{self.namn} leker glatt")

class Hund(Djur):
    def __init__(self, namn, födelseÅr):
        super().__init__(namn, födelseÅr)
    def ljud(self):
        print(f"{self.namn} låter WOOF WOOF MF!")
    def mata(self):
        print(f"{self.namn} äter glatt!")
    def lek(self):
        print(f"{self.namn} jagar bollen!")

class Katt(Djur):
    def __init__(self, namn, födelseÅr):
        super().__init__(namn, födelseÅr)
    def ljud(self):
        print(f"{self.namn} låter MJAU MJAU!")
    def mata(self):
        print(f"{self.namn} äter kräset...")
    def lek(self):
        print(f"{self.namn} jagar snörret")

class Fågel(Djur):
    def __init__(self, namn, födelseÅr):
        super().__init__(namn, födelseÅr)
    def ljud(self):
        print(f"{self.namn} låter KVITTER KVITTER!")
    def mata(self):
        print(f"{self.namn} pickar på frön")
    def lek(self):
        print(f"{self.namn} jagar möss")

djurLista = []

djurLista.append(Katt("Simba",2019))
djurLista.append(Katt("Luna",2021))
djurLista.append(Hund("Bella",2015))
djurLista.append(Hund("Max",2023))
djurLista.append(Fågel("Pip",2024))
djurLista.append(Fågel("Tove",2025))

for i in range(len(djurLista)):
    djurLista[i].ljud()
    djurLista[i].beskrivning()
    djurLista[i].mata()
    djurLista[i].lek()
