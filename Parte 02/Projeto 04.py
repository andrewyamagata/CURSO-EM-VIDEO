#Alistamento militar
import datetime
ano = int(input('Ano de nascimento: '))
idade = datetime.date.today().year - ano
print('Quem nasceu em {} tem {} anos'.format(ano, idade))