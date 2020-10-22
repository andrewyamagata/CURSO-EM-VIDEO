#Tabuada v3
while True:
    n = int(input('Digite qual tabuada você quer: '))
    print('-'*30)
    if n < 0:
        print("PROGRAMA ENCERRADO")
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)