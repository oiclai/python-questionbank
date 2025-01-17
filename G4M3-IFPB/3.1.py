n = int(input())
lista = []
for _ in range(n):
    pessoa = int(input())
    lista.append(pessoa)
lista_ordenada = sorted(lista)
for pessoas in lista_ordenada:
    print(pessoas)