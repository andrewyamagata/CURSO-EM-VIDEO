#Progressão Aritmética v2
"""print("Gerador de PA")
print("-="*12)
primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão da PA: "))
termo = primeiro
cont = 1
while cont <= 10:
    print("{} ->".format(termo),end=" ")
    termo += razão
    cont += 1
print("Fim")"""

#Progressão Aritmética v3
print("Gerador de PA")
print("-="*12)
primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão da PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} ->".format(termo),end=" ")
        termo += razão
        cont += 1
    print("Pausa")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print("PA finalizada com {} termos mostrados".format(total))