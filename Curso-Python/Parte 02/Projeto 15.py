#Grupo
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input("Em que ano a {}° pessoa nasceu? ".format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print("Ao total temos {} pessoas maiores de idade e {} menores de idade".format(totmaior,totmenor))

#Maior e menor da sequência
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Peso da {}° pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {} Kg'.format(maior))
print('O menor peso é {} Kg'.format(menor))