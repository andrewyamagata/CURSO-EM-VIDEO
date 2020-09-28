print("Olá Mundo")
print(7+4)
print('7'+'4')

nome = input('Qual o seu nome?')
ano = int(input('Em que ano você nasceu?'))
idade = 2020 - ano
print('Olá',nome,'você está com',idade,'de idade')
print('Está ficando velho meu amigo, {} anos já!'.format(idade))

a = input('Digite algo:')
print('O tipo primitivo desse valor é ', type(a))
print('É alfanumérico? ',a.isalnum())
print('É alfabético? ',a.isalpha())
print('É numérico? ', a.isnumeric())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
