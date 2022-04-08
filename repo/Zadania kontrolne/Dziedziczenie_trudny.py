class Budynek:
    def __init__(self, dlugosc, szerokosc, wysokosc, cena):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.cena = cena
    def obliczPowierzchnie(self):
        return self.dlugosc * self.szerokosc
    def obliczObjetosc(self):
        return self.dlugosc * self.szerokosc*self.wysokosc
    def cenaZaMetr(self):
        return self.cena / self.obliczPowierzchnie()

class Garaz(Budynek):
    def __init__(self, dlugosc, szerokosc, wysokosc, cena, ileSamochodow):
        super().__init__(dlugosc, szerokosc, wysokosc, cena)
        self.ileSamochodow = ileSamochodow
class Dom(Budynek):
    def __init__(self, dlugosc, szerokosc, wysokosc, cena, ilePokoi):
        super().__init__(dlugosc, szerokosc, wysokosc, cena)
        self.ilePokoi = ilePokoi


garaz = Garaz(int(input('Podaj dlugość garażu:')), int(input('Podaj szerokość garażu:')), int(input('Podaj wysokość garażu:')),int(input('Podaj ilosc samochodów:')), input('Podaj cenę garażu:'))
dom = Dom(int(input('Podaj dlugość domu:')), int(input('Podaj szerokość domu:')), int(input('Podaj wysokość domu:')), int(input('Podaj ilość pokoi:')), input('Podaj cenę domu:'))

print('Powierzchnia garażu:', garaz.obliczPowierzchnie())
print('Powierzchnia domu:', dom.obliczPowierzchnie())
print('Objetość garazu:', garaz.obliczObjetosc())
print('Objetość domu:', dom.obliczObjetosc())
print('Garaż, cena z metr:', garaz.cenaZaMetr())
print('Dom, cena z metr:', dom.cenaZaMetr())
