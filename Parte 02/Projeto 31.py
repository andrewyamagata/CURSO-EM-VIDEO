#Estatítica em produtos
print('-'*50)
print('{:^50}'.format('LOJA SUPER BARATÃO'))
print('-'*50)
total = contmais = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        contmais += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' ' #resp recebe vazio
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('O total gasto foi de {:.2f}'.format(total))
print(f'{contmais} produtos custam mais de R$ 10000,00')
print('{:-^50}'.format('FIM DO PROGRAMA'))