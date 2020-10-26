#Análise de dados do grupo
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF'  #enquanto não digitar M ou F
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]