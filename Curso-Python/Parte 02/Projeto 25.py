#maior e menor valores
opcao = "S"
soma = cont = media = maior = menor = 0
while opcao == "S":
    n = int(input("Digite um número: "))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    opcao = str(input("Quer continuar [S/N]? ")).strip().upper()[0]#[]0 considera 1° letra
media = soma / cont
print("Você digitou {} e a média foi {}".format(cont,media))
print("O maior número foi {} e o menor número foi {}".format(maior,menor))