# arvore = grafo ( raiz -> folhas) sem ciclo;
# 7 nós; 
# arvore binaria cada no tem 2 filhos;
n = int(input())
for i in range(n):
    v = list(map(int, input().split()))
    s1 = v[0] + v [1] + v[3]
    s2 = v[0] + v[1] + v[4]
    s3 = v[0] + v[2] + v[5]
    s4 = v[0] + v[2] + v[6]

    print(max(max(s1, s2), max(s3, s4)))

