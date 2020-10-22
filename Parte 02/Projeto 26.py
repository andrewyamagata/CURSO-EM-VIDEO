#Interrompendo repetições while
cont =1
while cont != 10:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')
#nao ser infinito

nome = 'Jose'
idade = 33
print('O %s tem %d anos. Forma 03' % (nome, idade)) #Python 2
print(f'O {nome} tem {idade} anos. Forma 01') #Python 3.6+
print('O {} tem {} anos. Forma 2', format(nome, idade)) #Python 3
