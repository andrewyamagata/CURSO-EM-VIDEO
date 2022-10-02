#Criando um menu de opções
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor:'))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input(">>>>> Qual é a sua opção: "))
    if opcao == 1:
        soma = n1 + n2
        print("A soma entre {} + {} é igual a {}".format(n1,n2,soma))
    elif opcao == 2:
        produto = n1 * n2
        print("A multiplicação entr {} x {} é igual a {}".format(n1,n2,produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        elif n1 < n2:
            maior = n2
        else:
            maior = "Os dois são iguais"
        print("O maior valor entre {} e {} é {}".format(n1,n2,maior))
    elif opcao == 4:
        print('Informe os valores novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print("Finalizando")
    else:
        print('Opção inválida. Tente novamente')
    print("=-="*10)
    sleep(1)
print("Done")