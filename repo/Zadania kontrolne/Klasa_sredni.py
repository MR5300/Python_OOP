class Osoba:
    def __init__(self, imie, nazwisko, wiek, hobby):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.hobby = hobby

znak = ''
osoby = []

while znak!='n':
    osoba = Osoba(input('Podaj imię: '), input('Podaj nazwisko:'), int(input('Podaj wiek:')), input('Podaj hobby:'))
    osoby.append(osoba)
    znak = input('Czy chcesz kontynuować? [t/n]')

for osoba in osoby:
    print('Imie:', osoba.imie)
    print('Nazwisko:', osoba.nazwisko)
    print('Wiek:', osoba.wiek)
    print('Hobby:', osoba.hobby, '\n')