class KontoBankowe:
    def __init__(self, nrRachunku,waluta):
        self.__nrRachunku = nrRachunku
        self.__waluta = waluta
        self.__saldo = 0
        self.__zalogowany = 0
    #Getter stanu konta
    def sprawdzStanKonta(self):
        print('Twoje saldo wynosi', self.__saldo, self.__waluta)
        return self.__saldo
    def wyplacKwote(self, kwota):
        if self.__saldo<kwota:
            print('Odmowa. Brak wystarczających środków na koncie!')
            return 0
        else:
            self.__saldo-=kwota
            print('Pomyślnie wypłacono', kwota, self.__waluta,)
            return 1
    def wplacKwote(self, kwota):
        self.__saldo+=kwota
        print('Pomyślnie wpłacono', kwota, self.__waluta)
    #Getter numeru konta
    def pokazNrRachunku(self):
        print('Twój numer rachunku to:', self.__nrRachunku)
        return self.__nrRachunku

konto = KontoBankowe('123456', 'zł')

konto.pokazNrRachunku()

konto.wplacKwote(300)
konto.sprawdzStanKonta()
konto.wyplacKwote(150)
konto.sprawdzStanKonta()
#Próba zmiany stanu konta z zewnątrz
konto.__saldo = 0
konto.sprawdzStanKonta()
