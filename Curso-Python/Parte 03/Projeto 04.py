#Maior e menor valores em Tupla
from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10))
"""print(f'Eu sorteei os valores {n}') -- usar com n"""
print('os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')