class Budynek:
    def __init__(self, dlugosc, szerokosc):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
    def obliczPowierzchnie(self):
        return self.dlugosc * self.szerokosc

class Garaz(Budynek):
    def __init__(self, dlugosc, szerokosc, ileSamochodow):
        super().__init__(dlugosc, szerokosc)
        self.ileSamochodow = ileSamochodow
class Dom(Budynek):
    def __init__(self, dlugosc, szerokosc, ilePokoi):
        super().__init__(dlugosc, szerokosc)
        self.ilePokoi = ilePokoi


garaz = Garaz(10, 2, 2)
dom = Dom(10, 10, 5)

print('Powierzchnia garażu:', garaz.obliczPowierzchnie())
print('Powierzchnia domu:', dom.obliczPowierzchnie())
