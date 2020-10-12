#Cálculo de fatorial
"""from math import factorial
n = int(input("Digite um número para calcular o seu fatorial: "))
f = factorial(n)
print("O fatorial de {} é {}".format(n,f))"""

print("Digite um número para calcular o seu ",end="")
fatorial = int(input("fatorial: "))
contador = fatorial
resultado = 1 #começar a multiplicalção limpa, começa com 1
print("Calculando o {}! => ".format(fatorial),end="")
while contador > 0:
    print("{}".format(contador), end="")
    print(' x 'if contador > 1 else " = ",end="")
    resultado *= contador
    contador -= 1
print("{}".format(resultado))
