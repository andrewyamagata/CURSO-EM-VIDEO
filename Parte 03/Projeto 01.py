#Tuplas, variável composta entre parenteses, são imutáveis
lanche = ('hambúrger', 'suco', 'pizza', 'pudim')
print(lanche) #todos os itens
print(lanche[3]) #item na posição 4 (item 3)
print(lanche[-1])#de trás p frente
print(lanche[:2]) #vai do 0 até o 1, ignorando o ultimo elemente, neste caso o 2
print(lanche[1:3])#vai do 1 até o 2 , ignorando o ultimo elemento, neste caso o 3
print(len(lanche))
for c in lanche:
    print(f'Como {c}')

for cont in range(0, len(lanche)):
    print(f'Eu comi{lanche[cont]}')