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

plik = open('dane.txt','a')
for osoba in osoby:
    plik.write(osoba.imie + ';' + osoba.nazwisko + ';' + str(osoba.wiek) + ';' + osoba.hobby + '\n')

plik = open('dane.txt', 'r')
for linia in plik:
    text = linia.split(';')
    print('Imie:', text[0])
    print('Nazwisko:', text[1])
    print('Wiek:', text[2])
    print('Hobby:', text[3])


