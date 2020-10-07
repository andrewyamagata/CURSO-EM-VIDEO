#Aumentos múltiplos
salario = float(input('Qual o seu salário? R$'))
if  salario > 1250:
    nsalario =  salario * 1.1
else:
    nsalario = salario * 1.15
print('O aumento do seu salário será de R$ {:.2f}'.format(nsalario))