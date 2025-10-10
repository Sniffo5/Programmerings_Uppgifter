class Bok:

    antal_böcker = 0
    _hemlig_kod = 0
    __hemligaste_kod = 0

    def __init__(self, titel, författare, utgivningsår):
        self.titel = titel
        self.författare = författare
        self.utgivningsår = utgivningsår
        Bok.antal_böcker += 1

    def __str__(self):
        return f" {self.titel}, utgiven år {self.utgivningsår} av {self.författare}"
    
    @classmethod
    def visa_antal_böcker(self):
        print(f" Det finns {self.antal_böcker} st böcker")
    
    @staticmethod
    def är_gammal_bok(år):
        if år < 1900:
            print("Ja, det är en gammal bok")
        else:
            print("Nej, det är inte en gammal bok")

bok1 = Bok("Frankenstein", "Mary Shelly", 1818)
bok2 = Bok("1984", "George Orwell", 1949)
bok3 = Bok("Band of Brothers", "Stephan E. Embrose", 1992)

Bok.visa_antal_böcker()
Bok.är_gammal_bok(1899)
Bok.är_gammal_bok(1927)

print(Bok._hemlig_kod)
print(Bok._Bok__hemligaste_kod)

    
