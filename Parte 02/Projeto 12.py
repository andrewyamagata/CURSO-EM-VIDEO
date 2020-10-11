#tabuada Versão 2
num = int(input('Digite um número para ver sua tabuada: '))
print("-="*6)
for c in range(1,11):
    print("{} x {:2} = {}".format(num,c,num * c))#{:2}todos vao ter 2 digitos, para ficar alinhado