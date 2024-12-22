colunas = int(input())
linha1 = list(map(int, input().split()))
linha2 = list(map(int, input().split()))
finallinha = []
for j in range(colunas):
    if linha1[j] > linha2[j]:
        finallinha.append(linha1[j])
    else:
        finallinha.append(linha2[j])
print(*finallinha)