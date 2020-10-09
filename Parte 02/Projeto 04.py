#Alistamento militar
import datetime
ano = int(input('Ano de nascimento: '))
idade = datetime.date.today().year - ano
print('Quem nasceu em {} tem {} anos'.format(ano, idade))
if idade > 18:
    print('Você deveria ter se apresentado no alistamento há {} anos atrás'.format(idade - 18))
elif idade < 18:
    print('Você ainda irá se alistar daqui {} anos'.format(18 - idade))
else:
    print('Você já tem {} anos, este ano você deve se alistar'.format(idade))