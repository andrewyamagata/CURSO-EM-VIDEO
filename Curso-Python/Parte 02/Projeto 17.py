#Estrutura de repetição while
c = 1
while c != 10:
    print(c,end=" ")
    c +=1
print("Acabou")

d = 1
while d != 0:
    d = int(input('Digite um número:'))
print("Acabou")

r = "S"
while r == "S":
    n = int(input('Digite um valor: '))
    r = str(input('Você deseja continuar? [S/N] ').upper())
print("End")