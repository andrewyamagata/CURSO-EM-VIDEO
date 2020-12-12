lista = ['abc', ['d'], ['ef']]
print(lista[2][0][0])


class Fracao:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __repr__(self):
        return str(self.num) + '/' + str(self.den)


f1 = Fracao(1, 2)
f2 = Fracao(3, 4)
print(f1)
print(f2)


class HORARIO:
    def __init__(self, hora, minu, segundo):
        self.hora = hora
        self.minu = minu
        self.segundo = segundo

    def __repr__(self):
        return str(self.hora) + ':' + str(self.minu) + ':' + str(self.segundo)


h = HORARIO(6, 28, 45)
print(h)