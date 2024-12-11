n = int(input())
for i in range(n):
    numeros = list(map(int, input().split()))  
    listaSomas = set() 
    somaRepetida = False
    for x in range(5): 
        for j in range(x + 1, 5): 
            valor = numeros[x] + numeros[j]
            if valor in listaSomas:
                print('YES')
                somaRepetida = True
                break
            listaSomas.add(valor) 
        if somaRepetida:
            break
    if not somaRepetida:
        print('NO')
