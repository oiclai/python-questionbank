linhas = int(input())
impressoes = []
caracteres = 0
for i in range(linhas):
    string = input()
    if len(string) + caracteres <= 144:
        impressoes.append(string)
        caracteres += len(string)
for impressao in impressoes:
    print(impressao)
