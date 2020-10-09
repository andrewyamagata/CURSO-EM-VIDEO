#Gerenciador de Pagamento
print('{:=^50}'.format(" LOJA YAMAGATA "))
preco = float(input("Preço das compras R$ "))
print('''Formas de Pagamento
[ 1 ] À Vista dinheiro/cheque
[ 2 ] À Vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual a sua opção: '))
if opcao == 1: #10% de desconto
    print('O valor final ficou em R$ {:.2f}'.format(preco*0.9))
elif opcao == 2: #5% de desconto
    print('O valor final ficou em R$ {:.2f}'.format(preco*0.95))
elif opcao == 3:
    print('O valor ficou em 2x de R$ {:.2f}'.format(preco/2))
elif opcao == 4:
    nvezes = int(input('Em quantas vezes você irá fazer? '))
    if  nvezes <= 2:
        print('Opção inválida')
    else:
        print('O valor ficou em {}x de R$ {:.2f}'.format(nvezes,(preco*1.2)/nvezes))
else:
    print('Opção inválida')