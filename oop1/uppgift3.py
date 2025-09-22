class Bankkund:
    def __init__(self, namn, saldo, id):
        self.namn = namn
        self.saldo = saldo
        self.transaktioner = ""
        self.id = (1000 + id)
    def insättning(self, insättning):
        if insättning <= 0:
            print(f"{insättning} är en otillåten insättnings summa")
        else:
            print(f"{self.namn} har {self.saldo} kr på kontot innan insättningen\n")
            temp = self.saldo
            self.saldo += insättning
            print(f"{self.namn} har {self.saldo} kr på kontot efter insättningen\n")
            self.transaktioner += f" {self.namn} hade {temp} kr på kontot innan de satt in {insättning} kr och därefter hade {self.saldo} kr\n"
    def uttag(self, uttag):
        if self.saldo >= uttag - 5000:
            print(f"{self.namn} har {self.saldo} kr på kontot innan uttaget\n")
            temp = self.saldo
            self.saldo -= uttag
            print(f"{self.namn} har {self.saldo} kr på kontot efter uttaget\n")
            self.transaktioner += f" {self.namn} hade {temp} kr på kontot innan de tog ut {uttag} kr och därefter hade {self.saldo} kr\n"
        else:
            print(f"{self.namn} har för lite saldo för ett uttag på {uttag} kr\n")
    def överföring(self, överföringStorlek, mottagare):
        if self.saldo >= överföringStorlek:
            print(f"\n{self.namn} har {self.saldo} kr på kontot innan de har överfört pengar\n")
            temp = self.saldo
            print(f"{mottagare.namn} har {mottagare.saldo} kr på kontot innan de har fått överföringen\n")
            self.saldo -= överföringStorlek
            mottagare.saldo += överföringStorlek
            print(f"{self.namn} har {self.saldo} kr på kontot efter de har överfört pengar\n")
            print(f"{mottagare.namn} har {mottagare.saldo} kr på kontot efter de har fått överföringen\n")

            self.transaktioner += f"{self.namn} hade {temp} kr på kontot innan de överförde {överföringStorlek} kr till {mottagare.namn} och därefter hade {self.saldo} kr\n"
        else:
            print(f" {self.namn} har inte tillräckligt mycket för en överföring på {överföringStorlek}")
    def ränta(self, procent):
        print(f"\n{self.namn} har {self.saldo} kr på kontot innan de har fått ränta\n")
        temp = self.saldo
        self.saldo *= (procent/100 + 1)
        print(f"{self.namn} har {self.saldo} kr på kontot efter de har fått {procent}% ränta\n")
        self.transaktioner += f" {self.namn} hade {temp} kr på kontot innan de fick {procent}% ränta och därefter hade {self.saldo} kr\n"
    def visaSaldo(self):
        print(f"{self.namn} innehavar {self.saldo} kr på deras konto\n")
    def visaTransaktioner(self):
        if self.transaktioner != "":
            print(f"\n{self.namn} har gjort dessa transaktioner:\n {self.transaktioner}")
        else:
            print(f"{self.namn} har inte gjort några transaktioner ännu\n")

class Bank:
    def __init__(self, name):
        self.name = name
        self.kundLista = []

    def läggTillKund(self, kund):
        self.kundLista.append(kund)

    def totalSaldo(self):
        total = 0
        for kund in self.kundLista:
            total += kund.saldo
        print(f"Totala saldot i banken är {total} kr")

    def hittaKundNamn(self,namn):
        for kund in self.kundLista:
            if kund.namn == namn:
                print(f"{kund.namn} har {kund.saldo} kr på kontot")
        pass
    def hittaKundID(self,id):
        for kund in self.kundLista:
            if kund.id == id:
                print(f"{kund.namn} har {kund.saldo} kr på kontot")
        pass



kundLista = []
bankTotal = 0

kundLista.append(Bankkund("Peter Persson", 22000, 1))
kundLista.append(Bankkund("Gunilla Johansson", 770000, 2))
kundLista.append(Bankkund("Sven-Gunnar Robinson", 1200000, 3))
kundLista.append(Bankkund("Jöns Jönsson", 2000, 4))
kundLista.append(Bankkund("Petra", 27000000, 5))
kundLista.append(Bankkund("Gunnar Johansson", 830000, 6))


