nome = str(input('Digite o seu nome:')).strip() #elimina já os espaços
print('O seu nome em maiúsculo é {}'.format(nome.upper()))
print('O seu nome em minúsculo é {}'.format(nome.lower()))
print('O seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) #conta tudo e subitrai os espaços
print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) #localizar onde está o primeiro espaço em branco
separa = nome.split() #separar entre espaços, cria lista
print('Seu primeiro nome tem {} letras e é {}'.format(len(separa[0]),separa[0])) #conta o item 0 da lista, mostra o que tem na lista 0
