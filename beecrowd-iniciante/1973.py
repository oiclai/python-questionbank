numeroDeEstrelas= int(input())
carneirosRoubados = 0
carneiros = list(map(int, input().split()))
totalAntesDaLoucura = sum(carneiros)
estrelaAtual = 0 # relação posicional
visitados = []
# estrelasVisitadas = 0
while 0 <= estrelaAtual < numeroDeEstrelas:
    # estrelasVisitadas+=1
    if carneiros[estrelaAtual] % 2 == 0: # n - 1
        if estrelaAtual not in visitados:
            visitados.append(estrelaAtual)
        carneiros[estrelaAtual]-=1
        carneirosRoubados+=1
        estrelaAtual-=1
                    
    elif carneiros[estrelaAtual] % 2 != 0: # n + 1
        if estrelaAtual not in visitados:
            visitados.append(estrelaAtual)
        carneiros[estrelaAtual]+=1
        carneirosRoubados+=1
        estrelaAtual+=1
        
numeroDeEstrelasVisitadas = len(visitados)
# print(visitados)
print(numeroDeEstrelasVisitadas)
print(totalAntesDaLoucura - carneirosRoubados)