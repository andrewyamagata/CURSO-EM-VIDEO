#Detector de Palíndromo
frase = str(input("Digite uma palavra ou frase: ")).strip().upper() #tira os espaços direita e esquerda, e deixa em maiúsculo
palavras = frase.split() #dividir a frase em palavras
junto = ''.join(palavras) #junta as palavras sem espaço
inverso = ''
for letra in range(len(junto) - 1, -1, -1): #(len de junto - 1* comecar a ultima letra, ir até a ultima letra -1, ir diminuindo
    inverso += junto[letra]
print("Você digitou {}, seu inverso é {}".format(junto, inverso))
if inverso == junto:
    print("TEMOS UUM PALÍNDROMO")
else:
    print("NÃO TEMOS UM PALÍNDROMO")
'''Pode ser feito com o macete do fatiamento'''
'''inverso = junto [::-1] => começa do início até o fim de trás p frente'''

