class Figura:
    def __init__(self, a, b):
        self._a = a
        self._b = b
    def obliczPole(self):
        pass

class Kwadrat(Figura):
    def __init__(self,a):
        super().__init__(a,a)
        self._h = a
    def obliczPole(self):
        return self._a**2

class Prostokat(Figura):
    def obliczPole(self):
        return self._a * self._b

class Trojkat(Figura):
    def __init__(self, a, h):
        self._a = a
        self._h = h
    def obliczPole(self):
        return self._a * self._h * 0.5

kwadrat = Kwadrat(5)
print('Pole kwadratu wynosi:',kwadrat.obliczPole())

prostokat = Prostokat(5, 5)
print('Pole prostokąta wynosi:',prostokat.obliczPole())

trojkat = Trojkat(5, 5, 5, 5)
print('Pole trójkąta wynosi:', trojkat.obliczPole())