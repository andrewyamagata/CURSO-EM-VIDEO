#Analisando Triângulos
l1 = float(input('Digite a medida do primeiro lado: '))
l2 = float(input('Digite a medida do segundo lado: '))
l3 = float(input('Digite a medida do terceiro lado: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos formam um Triângulo')
    if l1 == l2 and l2 == l3 and l1 == l3:
        print("EQUILÁTERO")
    elif l1 != l2 and l2 != l3 and l1 != l3:
        print("ESCALENO")
    else:
        print("ISÓSCELES")
else:
    print('Os segmentos NÃO formam um Triângulo')