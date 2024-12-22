numeroAntenas = int(input())
antenas = list(map(int, input().split()))
antenas.sort()
simounao = False
valor = antenas[1] - antenas[0]
for i in range(numeroAntenas-1):
    simounao = False
    if antenas[i+1] - antenas[i] == valor:
        simounao = True
if simounao:
    print('TRUE')
else:
    print('FALSE')
