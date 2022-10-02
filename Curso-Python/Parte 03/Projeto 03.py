#Tuplas com Times de Futebol

times = ('São Paulo','Palmeiras','Santos','Flamengo','Fortaleza','Bragantino')
print('-='*15)
print(f'Lista de times do Brasileirão: {times}')
print('-='*15)
print(f'Os 3 primeiros são {times[0:3]}')
print('-='*15)
print(f'Os 2 últimos são {times[-2:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*15)
print(f'O Fortaleza está na {times.index("Fortaleza")+1}ª posição')