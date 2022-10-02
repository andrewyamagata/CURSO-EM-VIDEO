#tabuada Versão 2
num = int(input('Digite um número para ver sua tabuada: '))
print("-="*6)
for c in range(1,11):
    print("{} x {:2} = {}".format(num,c,num * c))#{:2}todos vao ter 2 digitos, para ficar alinhado

#Soma dos pares
soma = 0
cont = 0
for d in range(1, 7):
    n = int(input('Digite o {}° valor: '.format(d)))
    if  n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('Você informou {} números PARES e a soma foi {}'.format(cont,soma))
