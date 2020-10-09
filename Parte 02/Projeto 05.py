#Clássico da Média
n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
media = (n1 + n2)/2
if  media >= 7:
    print('Você foi APROVADO com média {:.2f}'.format(media))
elif media < 5:
    print('Você foi REPROVADO com média {:.2f}'.format(media))
else: # media >= 5 and <7    OU    7 > media >= 5
    print('Você está de RECUPERAÇÃO com média {:.2f}'.format(media))