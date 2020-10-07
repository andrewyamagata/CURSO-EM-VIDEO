#Verificando as primeiras letras de um texto
cid = str(input('Em que cidade você nasceu? ')).strip() #eliminar os espaços
print(cid[:5].upper() == 'SANTO') #Verificar do inicio da string até o ponto 5, tudo em maiúsculo, se é igual a 'SANTO'

#Procurando uma string dentro de outra
nome = str(input('Qual o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))#'silva está em nome "tudo em minúsculo" - in é um operador python

#primeira e última ocorrência de uma string
frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes'.format(frase.upper().count("A")))#frase colocada em maipusculo e conta quanto "A" tem
print('A primeira letra A aparece na posição {}'.format(frase.upper().find("A") + 1))
print('A última letra A aparece na posição {}'.format(frase.upper().rfind("A")+1))

#Primeiro e último nome de uma pessoa
cnome = str(input('Digite o seu nome completo: ')).strip()
print('Muito prazer em te conhecer')
dcnome = cnome.split() #string será dividido em lista
print('Seu primeiro nome é {}'.format(dcnome[0]))
print('Seu último nome é {}'.format(dcnome[len(dcnome)-1])) #len vai ver a quantidade da lista e subitrai por 1 (começa sempre no 0)