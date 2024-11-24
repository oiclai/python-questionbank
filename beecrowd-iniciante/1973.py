numeroDeEstrelas= int(input())
carneiros = list(map(int, input().split()))
visitados = [0]*numeroDeEstrelas
numeroDeEstrelasVisitadas = 0
carneirosQueSobraram = 0
estrelaAtual = 0 

while 0 <= estrelaAtual < numeroDeEstrelas:
    if carneiros[estrelaAtual] % 2 == 1: # n + 1
        visitados[estrelaAtual] = 1
        carneiros[estrelaAtual] -= 1
        estrelaAtual += 1
    elif carneiros[estrelaAtual] % 2 == 0: # n - 1 
        if carneiros[estrelaAtual] > 0:
            visitados[estrelaAtual] = 1
            carneiros[estrelaAtual] -= 1
        estrelaAtual -= 1

for i in range(numeroDeEstrelas):
    carneirosQueSobraram += carneiros[i]
    numeroDeEstrelasVisitadas += visitados[i]

print(numeroDeEstrelasVisitadas, carneirosQueSobraram)