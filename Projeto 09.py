#Verificando as primeiras letras de um texto
cid = str(input('Em que cidade você nasceu? ')).strip() #eliminar os espaços
print(cid[:5].upper() == 'SANTO') #Verificar do inicio da string até o ponto 5, tudo em maiúsculo, se é igual a 'SANTO'

#Procurando uma string dentro de outra
nome = str(input('Qual o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))#'silva está em nome "tudo em minúsculo"
