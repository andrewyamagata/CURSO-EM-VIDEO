#JO-KEN-PO
import time
import random
lista = ("PEDRA","PAPEL","TESOURA")
pcopcao = random.randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
opcao = int(input('Qual a sua jogada? '))

time.sleep(1)
print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PO!")
time.sleep(1)
print('-='*15)
print('Computador jogou {}'.format(lista[pcopcao]))
print('Jogador jogou {}'.format(lista[opcao]))
print('-='*15)
if opcao == 0:
    if pcopcao == 0:
        print("EMPATE")
    elif pcopcao == 1:
        print("COMPUTADOR GANHOU")
    elif pcopcao == 2:
        print("JOGADOR GANHOU")
elif opcao == 1:
    if pcopcao == 0:
        print("JOGADOR GANHOU")
    elif pcopcao == 1:
        print("EMPATE")
    elif pcopcao == 2:
        print("COMPUTADOR GANHOU")
elif opcao == 2:
    if pcopcao == 0:
        print("COMPUTADOR GANHOU")
    elif pcopcao == 1:
        print("JOGADOR GANHOU")
    elif pcopcao == 2:
        print("EMPATE")
