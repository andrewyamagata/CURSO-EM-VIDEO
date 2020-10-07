#Condições (if - else)
#fazendo em if - else
tempo = int(input('Quantos anos tem o seu carro? '))
if tempo <= 3:
    print('Seu carro está novinho, pense em trocar daqui {} anos'.format(3 - tempo ))
else:
    print('Já está na hora de trocar o seu carro, ele está obsóleto faz {} anos'.format(tempo - 3))
print('----FIM----')

#pode ser feito de outra forma
tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo <= 3 else 'carro velho')
print('--END--')


#Jogo da adivinhação
import random #importar o random
import time #importar tempo de espera
print('-=' *30)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar... ")
print('-=' *30)
nescolhido = random.randint(0,5)
npensado = int(input("Em que número eu pensei? "))
print("Processando....")
time.sleep(3)
if nescolhido == npensado:
    print("Parabéns! Você acertou o número!")
else:
    print("Erooooou! Oloco bixo, você errou!")
print("Eu pensei no número {}".format(nescolhido))