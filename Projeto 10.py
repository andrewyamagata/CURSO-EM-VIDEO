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
