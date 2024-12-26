linhas, m = list(map(int, input().split()))
texto = []; questoezinhas = []
for i in range(linhas):
    palavras = input().split()
    texto.append(palavras)
qtd_questoes = int(input())
for j in range(qtd_questoes):
    questoes = input()
    questoezinhas.append(questoes)
# ------------------SAIDA---------------------
for x in range(len(texto)):
    if texto[x] in questoezinhas:
        
