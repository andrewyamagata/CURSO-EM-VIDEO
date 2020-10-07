#Aumentos múltiplos
salario = float(input('Qual o seu salário? R$'))
if  salario > 1250:
    nsalario =  salario * 1.1
else:
    nsalario = salario * 1.15
variacao = nsalario - salario
print('O seu salário de R$ {:.2f}, passará para R$ {:.2f}, aumento de R$ {:.2f}'.format(salario,nsalario,variacao))

#Analisando triângulos
print('-='*30)
print('Analisando Triângulo')
print('-='*30)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos formam um triângulo')
else:
    print('Os segmentos nao formam um triângulo')