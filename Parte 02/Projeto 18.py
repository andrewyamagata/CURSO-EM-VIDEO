#Validação de dados
s = str(input("Digite o seu sexo [F/M]: ")).strip().upper()[0] #pegar a primeira letra
while s not in "MF":
    s = str(input("Opção inválida. Digite novamente: ")).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(s))