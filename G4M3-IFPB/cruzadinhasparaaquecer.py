
# ta erradoooooooooooooooooooooooo
n = int(input())
for i in range(n):
    numeros = list(map(int, input().split()))
    listasomas = []
    proximo = 1
    for x in range(n):
        for j in range(n):
            if proximo >= n - 1:
                break
            valor = numeros[x] + numeros[proximo]
            proximo += 1
            listasomas.append(valor)
    for i in listasomas:
        if listasomas.count(i) > 1:
            print('YES')
            break
    else:
        print('NO')
