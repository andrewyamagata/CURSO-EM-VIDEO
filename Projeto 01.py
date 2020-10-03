print("Olá Mundo")
print(7+4)
print('7'+'4')

nome = input('Qual o seu nome?')
ano = int(input('Em que ano você nasceu?'))
idade = 2020 - ano
print('Olá',nome,'você está com',idade,'de idade')
print('Está ficando velho meu amigo, {} anos já!'.format(idade))
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))

a = input('Digite algo:')
print('O tipo primitivo desse valor é ', type(a))
print('É alfanumérico? ',a.isalnum())
print('É alfabético? ',a.isalpha())
print('É numérico? ', a.isnumeric())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())

# + adição
# - subtração
# * mutiplicação
# / divisão
# ** potência
# // divisão inteira
# % resto da divisão

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}'.format(n1+n2))
print('A soma vale {}, o produto vale {}, e a divisão vale {:.3}'.format(s,m,d)) #3 casas decimais
print('Divisão inteira {} e potência {}'.format(di,e))