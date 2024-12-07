n = int(input())
lista = list( map(int, input().split()) )
listaordenada = sorted(lista)
proximo = 1
for i in range(n):
  if proximo >= n - 1:
    print(listaordenada[-1]+1)
    break
  if listaordenada[i]+1 != listaordenada[proximo]:
    print(listaordenada[i]+1)
    break
  else:
    proximo+=1
