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

#[:5] Vai do 0 até 4 = Curso

#[15:] Vai do 15 até o Final = Python

#[9::3] Vai do 9 até o final, de 3 em 3 = VePh

#len(frase) qual o comprimento da frase, quantidade de caracteres = 21 caracteres

#frase.count('o'), mostra quantos 'o' tem = 3
#frase.count('o',0,13), conta quantos 'o', do 0 até 12 = 1
#frase.find('deo'), onde tem 'deo' = posição 11
#frase.find('Android'), não foi encontrado = -1
#'Curso' in frase => True
#frase.replace('Python','Android'), substitui Python em Android
#frase.upper() Deixar em Maiúsculo
#frase.lower() Deixar em Minúsculo
#frase.capitalize() Deixar a primeira em maiúsculo e o resto em minúsculo