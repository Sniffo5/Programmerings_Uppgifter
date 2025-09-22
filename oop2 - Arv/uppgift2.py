class Fordon:
    def __init__(self, märke, modell, år):
        self.märke = märke
        self.modell = modell
        self.år = år
    def beskrivining(self):
        return f"En {self.märke} {self.modell} {self.år} årsmodell"
    def är_veteran(self):
        if self.år <= 1995:
            return True
    
class Bil(Fordon):
    def __init__(self, märke, modell, år, antal_dörrar):
        super().__init__(märke, modell, år)
        self.antal_dörrar = antal_dörrar
    def beskrivining(self):
        return f"En {self.märke} {self.modell} {self.år} årsmodell med {self.antal_dörrar} st dörrar"

class Motorcykel(Fordon):
    def __init__(self, märke, modell, år, har_sidovagn):
        super().__init__(märke, modell, år)
        self.har_sidogvagn = har_sidovagn
    def beskrivining(self):
        if self.har_sidogvagn == True:
            return f"En {self.märke} {self.modell} {self.år} årsmodell med sidovagn"
        else:
            return f"En {self.märke} {self.modell} {self.år} årsmodell utan sidovagn"


fordonLista = []

fordonLista.append(Bil("Volvo", "V50", 2006, "5"))
fordonLista.append(Bil("Volvo", "S40", 2004, "5"))
fordonLista.append(Motorcykel("Kawasaki", "NINJA H2R", 2012, False))
fordonLista.append(Motorcykel("Harley Davidson", "ROAD GLIDE", 2025, True))

temp = 0
for i in range(len(fordonLista)):
    for j in range(len(fordonLista) -i -1):
        if fordonLista[j].år < fordonLista[j+1].år:
            temp = fordonLista[j]
            fordonLista[j] = fordonLista[j+1]
            fordonLista[j+1] = temp
    
for f in fordonLista:
    print(f.beskrivining())