repeticoes = int(input())
sensores = []
qtd_min_armadilhas = 0
sensoresJuntos = False
for i in range(repeticoes):
    sensor = int(input())
    sensores.append(sensor)

for sensor in sensores:
    if sensor == 1:
        if not sensoresJuntos: # se é false
            qtd_min_armadilhas += 1
            sensoresJuntos = True
    else:
        sensoresJuntos = False
print(qtd_min_armadilhas)


'''
5
1
1
0
1
0
Saida
2
'''
