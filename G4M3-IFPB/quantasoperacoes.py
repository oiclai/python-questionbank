n1, n2, n3 = map(int, input().split())
numeros = [n1, n2, n3]
numerosAposSorted = sorted(numeros)
min_trocas = 0
while numeros != numerosAposSorted:
    for i in range(len(numeros) - 1):
        if numeros[i] > numeros[i + 1]:
            numeros[i], numeros[i + 1] = numeros[i + 1], numeros[i]
            min_trocas += 1
print(min_trocas)
