#Estrutura de repetição for
#estrutura de laço repetição
for c in range(1, 6): #laço c=>"variavel de controle" no intervalo(1, 6), sem o 6
    #range(6,0,-1)começar do 6 até 0,
    print('OI')
    print(c)
print('FIM')
print(c)

#vai do 0 até o número escolhido +1
n = int(input('Digite um número: '))
for d in range(0, n+1):
    print(d)
print('Fim')

#Somatorio
s = 0
for e in range(0,4):
    n = int(input("Digite um valor: "))
    s = s + n #ou s += n
print('O somatório foi de {}'.format(s))