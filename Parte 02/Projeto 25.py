#maior e menor valores
cont = 0
while opcao == "S":
    n = int(input("Digite um número: "))
    opcao = str(input("Quer continuar [S/N]? ")).strip().upper()[0]#[]0 considera 1° letra
    cont += 1
print("Acabou")