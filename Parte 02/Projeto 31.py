#Estatítica em produtos
print('-'*50)
print('{:^50}'.format('LOJA SUPER BARATÃO'))
print('-'*50)
total = 0
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    total += preco

    resp = ' ' #resp recebe vazio
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('O total gasto foi de {:2f}'.format(total))
print('{:-^50}'.format('FIM DO PROGRAMA'))