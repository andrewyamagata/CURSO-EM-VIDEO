#Manipulando texto
#[] indica lista => começa em 0
#=>frase Curso em Video Python
frase = input('Digite:')

print(frase[9:13])
#[9:13] vai do 9 até o 12, o 13 não pega (ultimo valor nao pega), no caso = Vide

print(frase[9:21])
#[9:21] nao tem 21, vai até o ultimo, neste caso = Video Python

print(frase[9:21:2])
#[9:21:2] começa no 9 e para no 21, pulando de 2 em 2 = VdoPto

print(frase[:5])
#[:5] Vai do 0 até 4 = Curso

print(frase[15:])
#[15:] Vai do 15 até o Final = Python

print(frase[9::3])
#[9::3] Vai do 9 até o final, de 3 em 3 = VePh

print(len(frase))
#len(frase) qual o comprimento da frase, quantidade de caracteres = 21 caracteres

print(frase.count('o'))
#frase.count('o'), mostra quantos 'o' tem = 3

print(frase.count('o',0,13))
#frase.count('o',0,13), conta quantos 'o', do 0 até 12 = 1

print(frase.find('deo'))
#frase.find('deo'), onde tem 'deo' = posição 11

print(frase.find('Android'))
#frase.find('Android'), não foi encontrado = -1

print('Curso' in frase)
#'Curso' in frase => True

print(frase.replace('Python','Android'))
#frase.replace('Python','Android'), substitui Python em Android

print(frase.upper())
#frase.upper() Deixar em Maiúsculo

print(frase.lower())
#frase.lower() Deixar em Minúsculo

print(frase.capitalize())
#frase.capitalize() Deixar a primeira em maiúsculo e o resto em minúsculo

print(frase.title())
#frase.title() Deixa cada primeira palavra em maiúsculo

#frase.strip() Remove os espaços desnecessários da direita e esquerda da string
#frase.rstrip() Remove os espaços do lado direito da string
#frase.lstrip() Remove os espaços do lado esquerdo da string
#frase.split() onde tiver espaços vai dividir, cada palavra recebe uma indexação nova, divide uma string em uma lista
#'-'.join(frase) juntar os elementos da frase e coloca "-" em cada espaço
