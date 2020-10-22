#Interrompendo repetições while
cont =1
while cont != 10:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')

#nao ser infinito
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:    #se n for = 999, ele pausa e não conta
        break
    s += n
print('A soma vale {}'.format(s))

#f string
nome = 'Jose'
idade = 33
salario = 873.5
print(f'O {nome} tem {idade} anos. Forma 01') #Python 3.6+
print('O {} tem {} anos. Forma 02'.format(nome, idade)) #Python 3
print('O %s tem %d anos. Forma 03' % (nome, idade)) #Python 2
print(f'O sálario do {nome:^20}é de R$ {salario:.2f} ')#colocar o :.2f