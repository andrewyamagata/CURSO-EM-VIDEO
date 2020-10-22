#Tabuada v3
while True:
    n = int(input('Digite qual tabuada você quer: '))
    if n < 0:
        print("PROGRAMA ENCERRADO")
        break
    print('-'*30)
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)