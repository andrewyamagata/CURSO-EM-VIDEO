#Progressão Aritmética
print("="*20)
print("10 TERMOS DE UMA PA")
print("="*20)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10-1) * razao #achar o decimo termo
for c in range(termo,decimo + razao ,razao):
    print("{} ".format(c),end="- ")
print("\nAcabou")

#Números primos
numero = int(input("Digite um número: "))
cont = 0
for d in range(1,numero+1):
    if numero % d == 0:
        print("\033[33m", end=" ")
        cont = cont +1
    else:
        print("\033[31m", end=" ")
    print("{} ".format(d), end=" ")
if cont == 2:
    print("\n\033[34mO número {} é PRIMO".format(numero))
else:
    print("\n\033[36mO númeo {} não é PRIMO, sendo divisível por {} números".format(numero,cont))
