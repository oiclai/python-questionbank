'''
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
        '''
# bit mask = estrutura fixa c valores mudando
from itertools import permutations
n = int(input())
for i in range(n):
    v = list(map(int, input().split()))
    p = [1, 1, 1, 2, 2]
    ok = False 

    for perm in permutations(p):
        for j in range(5):
            c1 = 0
            c2 = 0

            if perm[1]== 1:
                c1 += v[j]
                c2+=v[j]
            else:
                continue

            for k in range(5):
                if k ==j:
                    continue
                if perm[k] == 1:
                    c1+=v[k]
                else:
                    c2+=v[k]

            if c1 == c2:
                ok = True
                break
            if ok:
                break
        print('YES' if ok else 'NO')
