#Comparando número
import time
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
time.sleep(2)
if  n1 > n2:
    print('O número {} é MAIOR que o número {}'.format(n1,n2))
elif n1 < n2:
    print('O número {} é MAIOR que o número {}'.format(n2,n1))
else:
    print('Os dois números são iguais')