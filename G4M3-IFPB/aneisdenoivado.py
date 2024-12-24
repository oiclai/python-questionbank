'''
 calcular o valor do anel, basta calcular o valor de cada um dos dez pedaços.
 E o valor de um pedaço é o valor do seu elo central somado com o valor do seu
 elo vizinho da esquerda somado com o valor do seu elo vizinho da direita
'''
    
def totalValor_anel(lista):
    totalSum = 0
    for i in range(10):
        pedaco = [lista[i %10], lista[(i + 1) %10], lista[(i + 2) %10]]
        pedacoSum = sum(pedaco)
        totalSum += pedacoSum
    return totalSum

conjunto_elo = []
for i in range(10):
    valorDoElo = int(input())
    conjunto_elo.append(valorDoElo)
total = totalValor_anel(conjunto_elo)
print(total)
