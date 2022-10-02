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
print("\nFim")

#Soma ímpares multiplos de três
soma = 0
cont = 0
for e in range(1, 501, 2): #só números ímáres
    if e % 3 == 0: #só múltiplos de 3
        cont = cont + 1 #cont += 1
        soma = soma + e #soma += e
        print(e, end=" ")
print("\nSomando os {} números, o valor total é {}".format(cont,soma))