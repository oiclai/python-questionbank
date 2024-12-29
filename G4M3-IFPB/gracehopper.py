n=int(input())
cont=0
analise=[]
for i in range(n):
    linha=input()
    analise.append(linha)
for linha in analise: # para cada linha dentro do vetor
    for caract in linha: # para cada caract na linha
        if caract=='B':
            cont+=1
if cont>0:
    print('YES')
else:
    print('NO')