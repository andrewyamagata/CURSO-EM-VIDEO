#Aumentos múltiplos
salario = float(input('Qual o seu salário? R$'))
if  salario > 1250:
    nsalario =  salario * 1.1
else:
    nsalario = salario * 1.15
variacao = nsalario - salario
print('O seu salário de R$ {:.2f}, passará para R$ {:.2f}, aumento de R$ {:.2f}'.format(salario,nsalario,variacao))