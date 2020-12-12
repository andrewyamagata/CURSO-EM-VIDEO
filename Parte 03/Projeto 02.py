#Número por extenso

lista = ('zero', 'um', 'dois', 'três', 'quatro',
         'cinco' , 'seis', 'sete' , 'oito', 'nove',
         'dez', 'onze', 'doze', 'treze', 'catorze',
         'quinze', 'dezesseis', 'dezessete', 'dezoito',
         'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20:  '))
    if n < 0 or n > 20:
        print('Tente novamente. ', end='')
    else:
        print(f'Você digitou o número {lista[n]}')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Desejá continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
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