beleza = 0
palavrasFinais = []
for _ in range(4):
    frase = input().strip()
    palavrasFinais.append(frase.split()[-1])
def calcular_beleza(palavra1:str, palavra2:str)->int:
    beleza=0 # errei querendo considerar beleza uma variavel global aqui
    tamanho_palavra1, tamanho_palavra2 = len(palavra1) - 1, len(palavra2) - 1
    while tamanho_palavra1 >= 0 and tamanho_palavra2 >= 0 and palavra1[tamanho_palavra1] == palavra2[tamanho_palavra2]:
        beleza += 1
        tamanho_palavra1 -= 1
        tamanho_palavra2 -= 1
    return beleza
# 0 2
# 1 3
beleza += calcular_beleza(palavrasFinais[0], palavrasFinais[2])
beleza += calcular_beleza(palavrasFinais[1], palavrasFinais[3])
print(beleza)