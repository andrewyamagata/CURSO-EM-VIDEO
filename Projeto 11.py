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