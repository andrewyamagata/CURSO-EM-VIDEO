#Condicional = radar eletrônico
velocidade = float(input('Qual a velocidade atual do carro? '))
if  velocidade <= 80:
    print('Dirija com segurança!')
else:
    print('Multado! Você excedeu o limite de velocidade de 80 km/h')
    print('Você deverá pagar uma multa de R$ {:.2f}'.format((velocidade - 80)*7))#número decimal com duas casas flutuante
print('Tenha um bom dia!')