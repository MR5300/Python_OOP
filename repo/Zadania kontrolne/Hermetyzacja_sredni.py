KURS_EURO = 4.64
KURS_DOLARA = 4.27

class KontoBankowe:
    def __init__(self, nrRachunku, waluta, pin):
        self._nrRachunku = nrRachunku
        self.__waluta = waluta
        self.__saldo = 0
        self.__zalogowany = 0
        self.__pin = pin
    def sprawdzStanKonta(self):
        if self.uwierzytelnienieUzytkownika():
            print('Twoje saldo wynosi', self.__saldo, self.__waluta)
            return self.__saldo
    def wyplacKwote(self, kwota):
        print(self.__saldo<kwota, self.__zalogowany)
        if self.uwierzytelnienieUzytkownika():
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
    def uwierzytelnienieUzytkownika(self):
        if self.__zalogowany != 1:
            pin = input('Podaj pin:')
            if pin == self.__pin:
                self.__zalogowany = 1
                return 1
            print('Niepoprawny pin!')
            return 0
        return 1
    def przelejPieniadze(self, konto, kwota):
        if self.wyplacKwote(kwota) == 1:
            konto.wplacKwote(kwota)
            print('Pomyślnie przelano pieniąze na konto o nr', konto.sprawdzNrKonta())
            return 1
        print('Nie udało się przelać pieniędzy')
    def sprawdzNrKonta(self):
        return self._nrRachunku



konto1 = KontoBankowe('123456', 'zł', '12345')

konto1.wplacKwote(300)
konto1.sprawdzStanKonta()
konto1.wyplacKwote(150)
konto1.sprawdzStanKonta()
#Próba zmiany stanu konta z zewnątrz
konto1.__saldo = 0
konto1.sprawdzStanKonta()

konto2 = KontoBankowe('654321', 'zł', '54321')

konto2.wplacKwote(5000)
konto2.sprawdzStanKonta()

konto2.przelejPieniadze(konto1, 500)
konto2.sprawdzStanKonta()