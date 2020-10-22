#Vários números com flag
n = c = s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    c += 1
    s += n
print(f"Você digitou {c} números e a some entre eles é igual a {s}")