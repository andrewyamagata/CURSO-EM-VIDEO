#Sorteando
import random
n1 = str(input('Primeiro aluno: ')) #string, não necessário colocar
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1,n2,n3,n4] #criar uma lista, deixar em colchetes
escolha = random.choice(lista) #escolhe uma variável aleatória
print('O aluno escolhido foi {}!'.format(escolha))

#Sorteio e colocar em ordem
random.shuffle(lista)
print('A ordem será:')
print(lista)
