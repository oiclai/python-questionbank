# dicionario = {}
# while True:
#     palavra = input()
#     if palavra == 'FIM':
#         break
#     if palavra not in dicionario:
#         dicionario[palavra] = 1
#     else:
#         dicionario[palavra]+=1
# for elemento in dicionario:
#     print(f"{elemento} {dicionario[elemento]}")

lista = []
while True:
    palavra = input()
    if palavra == 'FIM':
        break
    lista.append(palavra)
    print(f"{palavra} {lista.count(palavra)}")