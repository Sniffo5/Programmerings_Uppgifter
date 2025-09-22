class Rektangel:
    def __init__(self, bredd, längd):
        self.bredd = bredd
        self.längd = längd
    def area(self):
        return self.bredd * self.längd
    def omkrets(self):
        return (self.bredd * 2) + (self.längd * 2)
    
rektangel1 = Rektangel(2,3)

print(f"{rektangel1.area()}")
print(f"{rektangel1.omkrets()}")

rekangelLista = []

rekangelLista.append(Rektangel(1, 4))
rekangelLista.append(Rektangel(3, 5))
rekangelLista.append(Rektangel(11, 9))
rekangelLista.append(Rektangel(12, 14))
rekangelLista.append(Rektangel(2, 20))

for i in range(len(rekangelLista)):
    print(f"Bredd: {rekangelLista[i].bredd} & Längd: {rekangelLista[i].längd} ger en area på {rekangelLista[i].area()} och en omkrets på {rekangelLista[i].omkrets()}")