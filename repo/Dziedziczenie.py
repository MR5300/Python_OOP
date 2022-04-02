#Klasa bazowa
class Zwierze:
    #Kontruktor
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek
        self.przebytaOdleglosc = 0
    def idzDoPrzodu(self):
        self.przebytaOdleglosc+=5
        print('Twoje zwierze o imieniu: ', self.imie, ' porusza się do przodu')
    def sprawdzWiek(self):
        print('Wiek', self.imie, 'to', self.wiek, 'lat')

#Klasa pochodna
class Pies(Zwierze):
    def __init__(self, imie, wiek):
        super().__init__(imie, wiek)
        self.gatunek = 'Pies'
    def dajGłos(self):
        print('Hał, hał!')

#Klasa pochodna
class Kameleon(Zwierze):
    def __init__(self, imie, wiek):
        super().__init__(imie, wiek)
        self.gatunek = 'Kameleon'
    def zmienKolor(self, kolor):
        print('Twój kameleon zmienił kolor na ', kolor)

pies = Pies('Reksio', 6)
kameleon = Kameleon('Bob', 5)

pies.idzDoPrzodu()
pies.dajGłos()

kameleon.zmienKolor('czerwony')

print('Odleglosc przebyta przez psa:', pies.przebytaOdleglosc)
print('Odleglosc przebyta przez kameleona:', kameleon.przebytaOdleglosc)

pies.sprawdzWiek()
kameleon.sprawdzWiek()