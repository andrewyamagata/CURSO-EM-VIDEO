#Cores no Terminal
#ANSI (escape sequence)
#\033[_:_:_m => STYLE:TEXT:BACK
#style 0 none - 1 bold - 4 underline - 7 negative
#text 30 branco - 31 vermelho - 32 verde - 33 amarelo - 34 azul - 35 roxo - 36 aquarela - 37 cinza
#back 40 branco - 41 vermelho
print('\033[0:33:44mOlá, Mundo!')
print('\033[4:33:41m Olá Mundo\033[m')
nome = 'Andrew'
print('Olá, muito prazer {}{}{}. Bem vindo'.format('\033[1:34m', nome,'\033[m'))
#criando lista de cores
cores = {'limpa':'\033[m', 'azul':'\033[34m', 'amarelo':'\033[33m'}
print('Bom dia, {}{}{}. Bem vindo'.format(cores['amarelo'],nome,cores['limpa']))