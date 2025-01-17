n = int(input())

# Criar a matriz vazia
matriz = [[0 for _ in range(n)] for _ in range(n)]
numero = 1

# Definir o ponto inicial (centro para n ímpar, canto inferior direito para n par)
linha, coluna = n // 2, n // 2
if n % 2 == 0:
    coluna -= 1

# Preenchendo a matriz em espiral
for repeticao in range(1, n, 2):
    for _ in range(repeticao):  # Direita
        matriz[linha][coluna] = numero
        numero += 1
        coluna += 1
    for _ in range(repeticao):  # Cima
        matriz[linha][coluna] = numero
        numero += 1
        linha -= 1
    for _ in range(repeticao):  # Esquerda
        matriz[linha][coluna] = numero
        numero += 1
        coluna -= 1
    for _ in range(repeticao ):  # Baixo
        matriz[linha][coluna] = numero
        numero += 1
        linha += 1

# Exibir a matriz
for linha in matriz:
    print(*linha)

