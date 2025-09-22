class Film:
    def __init__(self, titel, betyg):
        self.titel = titel
        self.betyg = betyg

filmLista = []

filmLista.append(Film("The Godfather", 8.5)) 
filmLista.append(Film("Gladiator", 7))
filmLista.append(Film("Oppenheimer", 9.6))
filmLista.append(Film("The Dark Knight", 9.3))
filmLista.append(Film("Schindler's List", 9))
filmLista.append(Film("Matrix", 9.2))
filmLista.append(Film("1917", 9.1))

for i in range(len(filmLista)):
    print(f"{filmLista[i].titel} - {filmLista[i].betyg} / 10p \n")

