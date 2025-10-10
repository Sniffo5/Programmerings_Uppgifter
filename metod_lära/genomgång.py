class Bil:

    _antal_bilar = 0 # klassvariabel
    __superhemlig = 100

    def __init__(self, märke, färg):
         self.märke = märke #instansvariabel
         self.färg = färg
         self._antal_bilar += 1
    def __str__(self):
         return f"\nEn {self.färg} {self.märke}"
    
    @staticmethod #metoden tillhör klassen inte en instans
    def statisk_metod():
         print("Jag är ne statisk metod")
    
    @classmethod #metod som tillhör klassen, men kommer också åt medlemsklassns variabler.
    def klass_metod(cls):
         print(cls.__superhemlig)
    
b1 = Bil("Volvo", "svart")
b2 = Bil("Saab", "grön")

print(b1,b2)

Bil.klass_metod()