#Analisador completo
tidade = 0
midade = 0
mihomem = 0
nvelho = ''
tmulher = 0
for g in range(1,5):
    print("----- {}º PESSOA -----".format(g))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    tidade = tidade + idade
    if g == 1 and sexo in 'Mm':
        mihomem = idade
        nvelho = nome
    if sexo in 'Mn' and idade > mihomem:
        mihomem = idade
        nvelho = nome
    if sexo in 'Ff' and idade < 20:
        tmulher = tmulher + 1
midade = tidade / 4
print('A média de idade do grupo é de {} anos'.format(midade))
print('O homem mais velha é {} e tem {} anos'.format(nvelho,mihomem))
print('Ao todo são {} mulheres com menos de 20 anos'.format(tmulher))