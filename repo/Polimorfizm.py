class Mebel:
    def __init__(self, wysokosc, szerokosc, glebokosc, cena, sztuk):
        self._wysokosc = wysokosc
        self._szerokosc = szerokosc
        self._glebokosc = glebokosc
        self._cena = cena
        self._iloscSztuk = sztuk
    def dostawaMebli(self, ilosc):
        self._iloscSztuk+=ilosc
    def zakupMebli(self, ilosc):
        self._iloscSztuk+=ilosc
    def zaprezentujProdukt(self):
        print('Wysokość:', self._wysokosc)
        print('Szerokość:', self._szerokosc)
        print('Glebokość:', self._glebokosc)
        print('Cena:', self._cena)
        print('Dostępnych:', self._iloscSztuk, 'sztuk')
    def zaprezentujMebel(self):
        pass

class Biurko(Mebel):
    def __init__(self, wysokosc, szerokosc, glebokosc, cena, sztuk, iloscSzuflad, iloscPolek):
        super().__init__(wysokosc, szerokosc, glebokosc, cena, sztuk)
        self._iloscSzuflad = iloscSzuflad
        self._iloscPolek = iloscPolek
    def zaprezentujMebel(self):
        print('\nErgonomiczne biurko:')
        self.zaprezentujProdukt()
        print('Ilosc szuflad:', self._iloscSzuflad)
        print('Ilosc półek:', self._iloscPolek)

class Fotel(Mebel):
    def __init__(self, wysokosc, szerokosc, glebokosc, cena, sztuk, obrotowy, maxKg):
        super().__init__(wysokosc, szerokosc, glebokosc, cena, sztuk)
        self._obrotowy = obrotowy
        self._maksymalneObciazenie = maxKg
    def zaprezentujMebel(self):
        print('\nSuper wygodny fotel:')
        self.zaprezentujProdukt()
        print('Maksymalne obciążenie:', self._maksymalneObciazenie)
        print('Obrotowy:', self._obrotowy)
biurko = Biurko(1,1,1,1,20,1,1)
fotel = Fotel(1,1,1,1,40, 'TAK', 150)

meble = [biurko, fotel]

for mebel in meble:
    mebel.zaprezentujMebel()


