# Instalando módulos

#ceil arredonda p cima
#floor arredonda p baixo
#trunc truncar
#pow potencia
#sqrt raiz quadrada
#factorial fatorial

#importar tudo => import math
#importar funcionalidade especifica => from math import sqrt
#https://docs.python.org/pt-br/3.7/library/index.html biblioteca para importar
#ctrl + espaço mostra lista

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é {:.2f}!'.format(num, (raiz)))

import random
nrandom = random.randint(1,60)
print(nrandom)
'''from random import randint
nrandom = randint(1,60)      => não colocar random, já importou randint
print(nrandom)'''

#pypi módulos externos
# Settings -> Project: Python -> Python Interpreter -> +

angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo)) #transformar em radianos o angulo e achar o seno
print('O ângulo de {} tem o Seno de {:.2f}'.format(angulo,seno))
