class Pies:
    #Konstruktor
    def __init__(self, imie, wiek, rasa):
        #Pola
        self.imie = imie
        self.wiek = wiek
        self.rasa = rasa
    #Metoda
    def zaszczekaj(self):
        print('Hał, hał.')
#Definicja obiektu
pies = Pies('Reksio', 3, 'Lablador')

#Wypisanie wartości obiektu
print('Imię: ', pies.imie)
print('Wiek: ', pies.wiek, ' lata')
print('Rasa: ', pies.rasa)
#Wywołanie metody obiektu
pies.zaszczekaj()
