class Figura:
    def __init__(self, a, b):
        self._a = a
        self._b = b
    def obliczPole(self):
        pass

class Kwadrat(Figura):
    def __init__(self,a):
        super().__init__(a,a)
        self.h = a
    def obliczPole(self):
        return self._a**2

class Prostokat(Figura):
    def obliczPole(self):
        return self._a * self._b

kwadrat = Kwadrat(5)
print('Pole kwadratu wynosi:',kwadrat.obliczPole())

prostokat = Prostokat(5, 5)
print('Pole prostokąta wynosi:',prostokat.obliczPole())