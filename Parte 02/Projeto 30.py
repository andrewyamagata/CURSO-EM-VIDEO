#Análise de dados do grupo
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':  #enquanto não digitar M ou F
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]