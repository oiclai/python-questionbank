# nomes = set()
# for i in range(numero):
#     nome = input()
#     nomes.add(nome)
# for i in nomes:
#     print(i)

numero = int(input())
nomes = []
for i in range(numero):
    nome = input()
    if nome not in nomes:
        nomes.append(nome)
for j in nomes:
    print(j)
