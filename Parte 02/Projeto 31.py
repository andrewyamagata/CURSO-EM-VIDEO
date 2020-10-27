#Estatítica em produtos
print('-'*50)
print('{:^50}'.format('LOJA SUPER BARATÃO'))
print('-'*50)
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))

    resp = ' ' #resp recebe vazio
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print()