#Tratando vários valores
"""num = cont = soma = 0
while num != 999:
    num = int(input("Digite um número [999 para parar]: "))
    soma += num
    cont += 1
print("Você digitou {} números e a soma deu {}".format(cont-1,soma-999))"""

#pode ser feito dessa maneira
num = cont = soma = 0
num = int(input("Digite um número [999 para parar]: ")) #coloca a flag p fora
while num != 999:
    soma += num
    cont += 1
    num = int(input("Digite um número [999 para parar]: ")) #ler como última linha
print("Você digitou {} números e a soma deu {}".format(cont,soma))