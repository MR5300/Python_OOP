class Prostokat:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def obliczPole(self):
        return self.a*self.b
    def obliczObwod(self):
        return 2*self.a+2*self.b

class Kwadrat(Prostokat):
    def __init__(self,a):
        self.a = a
        self.b = a
figura = Kwadrat(2)

print('Pole:', figura.obliczPole())
print('Obwod:', figura.obliczObwod())
