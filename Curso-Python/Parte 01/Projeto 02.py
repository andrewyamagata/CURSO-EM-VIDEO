# + adição
# - subtração
# * mutiplicação
# / divisão
# ** potência
# // divisão inteira
# % resto da divisão

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}'.format(n1+n2))
print('A soma vale {}, o produto vale {}, e a divisão vale {:.3f}'.format(s,m,d)) #3 casas decimais
print('Divisão inteira {} e potência {}'.format(di,e))
print('A soma vale {}, o produto vale {}, e a divisão vale {:.3f}'.format(s,m,d), end=' ')#end=' ' não quebrar linha, colocar dentro da aspas
print('Divisão inteira {} e potência {}'.format(di,e))
print('A soma vale {}, \n o produto vale {}, \n e a divisão vale {:.3f}'.format(s,m,d)) #\n quebra linha
print('Divisão inteira {} e potência {}'.format(di,e))

n = int(input('Digite um valor: '))
print('antecessor {} e sucessor {}, ao número escolhido {}!'.format((n-1),(n+1),n))
print('Dobro {}\nTriplo {}\nRaiz quadrada {:.2f}!'.format((n*2),(n*3),(n**(1/2))))#pow(n, (1/2) também calcula raiz quadrada
