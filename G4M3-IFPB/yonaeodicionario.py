linhas, m = list(map(int, input().split()))
texto = [input().split() for _ in range(linhas)] # pra n ter q declarar uma lista vazia
qtd_questoes = int(input())
questoezinhas = [input() for _ in range(qtd_questoes)] # me familiarizar c list comprehesion
for questao in questoezinhas:
    for i in range(len(texto)):
        if questao in texto[i]:
            print(f"{questao} {i + 1}")
            break # codigo otimizado -> n precisa percorrer td matriz dps de ter encontrado









'''
----------------------- Entrada 1 ---------------------------
10 3
alga aram boro
caju coce cume
devo digo ergo
fole frio goma
ieis irei iris
miro mofe momo
note odia paro
poem safo seda
suco tope uiva
unta veto vida
5
goma
devo
suco
paro
veto
-------------------- Saida 1 -----------------------
goma 4
devo 3
suco 9
paro 7
veto 10
'''