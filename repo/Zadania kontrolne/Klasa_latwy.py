class Osoba:
    def __init__(self, imie, nazwisko, wiek, hobby):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.hobby = hobby

osoba = Osoba('Jan', 'Kowalski', 16, 'Sport')

print('Imie:', osoba.imie)
print('Nazwisko:', osoba.nazwisko)
print('Wiek:', osoba.wiek)
print('Hobby:', osoba.hobby)