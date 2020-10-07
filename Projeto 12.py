#Ano bissexto
import datetime #importar datas
ano = int(input('Que ano quer verificar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year    #ver a data do dia e pegar só o ano
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #ocorrendo a cada quatro anos (exceto anos múltiplos de 100 que não são múltiplos de 400)
    print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))