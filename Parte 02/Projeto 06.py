#Classíficando
from datetime import date
atual = date.today().year
ano = int(input('Em que ano você nasceu? '))
idade = atual - ano
if idade <= 9: #< depois =
    categoria = ("MIRIM")
elif idade <= 14:
    categoria = ("INFANTIL")
elif idade <=19:
    categoria = ("JUNIOR")
elif idade <= 25:
    categoria = ("SÊNIOR")
else:
    categoria = ("MASTER")
print("Você está com {} anos e a sua categoria é {}!".format(idade,categoria))