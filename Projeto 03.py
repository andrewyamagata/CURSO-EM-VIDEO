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

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é {:.2f}!'.format(num, (raiz)))