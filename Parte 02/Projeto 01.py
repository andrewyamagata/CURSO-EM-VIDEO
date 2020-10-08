#Condições Aninhadas
#if -> elif -> elif -> else # pode usar quantos elif quiser

#Aprovando Empréstimo
casa = float(input('Qual o valor da casa: R$ '))
salario = float(input('Qual o valor do salário: R$ '))
tempo = int(input('Quanto anos para pagar? '))
salario30 = salario * 0.30
prestacao = casa / (tempo * 12)
#if

print('Para pagar a casa de R$ {:.2f}, com o salário que recebe de R$ {:.2f}, em {} anos, você deve pagar mensalmente R$ {}'.format(casa,salario,tempo,prestacao))