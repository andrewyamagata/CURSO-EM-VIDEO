#Condicional = radar eletrônico
velocidade = float(input('Qual a velocidade atual do carro? '))
if  velocidade <= 80:
    print('Dirija com segurança!')
else:
    print('Multado! Você excedeu o limite de velocidade de 80 km/h')
    print('Você deverá pagar uma multa de R$ {:.2f}'.format((velocidade - 80)*7))#número decimal com duas casas flutuante
print('Tenha um bom dia!')

#Sabendo se é par ou ímpar
numero = int(input('Me diga um número: '))
resultado = numero % 2 #Resto da divisão 0 ou 1.
if  resultado == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é ÍMPAR'.format(numero))

#Custo de viagem
dviagem = float(input('Qual a distância da viagem? '))
print('Você está presete a começar uma viagem de {} Km'.format(dviagem))
if  dviagem <= 200:
    vpassagem = dviagem * 0.5
else:
    vpassagem = dviagem * 0.45
print('E o preço da sua passagem será de R$ {:.2f}'.format(vpassagem))

#Pode ser feito de outra maneira
distancia = float(input('Qual a distância da viagem? '))
preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45 #if na linha (if simplificado)
print('O preço da passagem será de R$ {:.2f}'.format(preco))
