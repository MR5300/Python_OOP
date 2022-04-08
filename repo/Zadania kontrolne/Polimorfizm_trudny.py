class Figura:
    def __init__(self, a, b):
        self._a = a
        self._b = b
    def obliczPole(self):
        pass
    def obliczObwod(self):
        pass

class Kwadrat(Figura):
    def __init__(self,a):
        super().__init__(a,a)
        self._h = a
    def obliczPole(self):
        return self._a**2
    def obliczObwod(self):
        return self._a*4

class Prostokat(Figura):
    def obliczPole(self):
        return self._a * self._b
    def obliczObwod(self):
        return self._a*2 + self._b*2

class Trojkat(Figura):
    def __init__(self, a, b, c, h):
        super().__init__(a, b)
        self._c = c
        self._h = h
    def obliczPole(self):
        return self._a * self._h * 0.5
    def obliczObwod(self):
        return self._a + self._b + self._c

kwadrat = Kwadrat(5)
print('Pole kwadratu wynosi:',kwadrat.obliczPole())
print('Obwód kwadratu wynosi:', kwadrat.obliczObwod())
print()

prostokat = Prostokat(5, 6)
print('Pole prostokąta wynosi:',prostokat.obliczPole())
print('Obwód prostokata wynosi:', prostokat.obliczObwod())
print()

trojkat = Trojkat(5, 5, 5, 5)
print('Pole trójkąta wynosi:', trojkat.obliczPole())
print('Obwód trojkata wynosi:',trojkat.obliczObwod())
