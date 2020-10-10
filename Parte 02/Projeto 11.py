#Contagem regressiva
import time
print('Contagem regressiva')
for c in range(10,-1, -1):
    print(c)
    time.sleep(0.5)
print("BUUUUUM")

#Contagem pares
for d in range(1,51): # ou range(2, 51, 2) de 2 até 50 pulando de 2 em 2, neste caso apresenta números pares
    if  d % 2 == 0:
        print(d, end=" ")