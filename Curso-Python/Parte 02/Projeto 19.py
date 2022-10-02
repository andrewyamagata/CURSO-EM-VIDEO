#Jogo da adivinhação
import random
computador = random.randint(0,10)
print('Sou seu computador.... Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Um pouco mais")
        elif jogador > computador:
            print('Um pouco menos')
print('Acertou!')
print('Você acertou com {} palpites. Parabéns'.format(palpite))