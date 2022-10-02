#Condições Aninhadas
#if -> elif -> elif -> else # pode usar quantos elif quiser

#Aprovando Empréstimo
casa = float(input('Qual o valor da casa: R$ '))
salario = float(input('Qual o valor do salário: R$ '))
tempo = int(input('Quanto anos para pagar? '))
salario30 = salario * 0.30
prestacao = casa / (tempo * 12)
if salario30 >= prestacao and tempo >= 15:
    print('Empréstimo não excede 30 % do seu sálario')
    print('-='*30)
    print('EMPRÉSTIMO APROVADO COM RESTRIÇÕES')
    print('-='*30)
elif salario30 >= prestacao and tempo < 15:
    print('Empréstimo não excede 30 % e pagará em ',tempo)
    print('-='*30)
    print('EMPRÉSTIMO APROVADO SEM RESTRIÇÕES')
    print('-='*30)
else:
    print('Empréstimo excede 30% do seu salário')
    print('-='*30)
    print('EMPRÉSTIMO NEGADO')
    print('-='*30)
print('Para pagar a casa de R$ {:.2f}.\nCom o salário que recebe de R$ {:.2f}.\nEm {} anos, você deve pagar mensalmente R$ {:.2f}'.format(casa,salario,tempo,prestacao))
#\n quebra linha
#end=' ' puxa a linha de baixo