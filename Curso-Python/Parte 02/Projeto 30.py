#Análise de dados do grupo
cont18 = contm = contf20 = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':  #enquanto não digitar M ou F
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade > 18:
        cont18 += 1
    if sexo == 'M':
        contm += 1
    if sexo == 'F' and idade < 20:
        contf20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar? [S/N} ")).strip().upper()[0]
    if resp == 'N':
        break
print(f'Do total {cont18} tem mais de 18 anos, {contm} são homens, {contf20} são mulheres com menos de 20 anos.')