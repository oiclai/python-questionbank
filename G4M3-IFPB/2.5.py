# posicao = 0
# meloesAtirados = 0
# while True:
#     fototirada = input()
#     # para encerrar
#     if 'X' not in fototirada:
#         break

#     # se o bicho tiver olhando p mim -> essa condição é independente
#     if fototirada[posicao] == 'X':
#         print("Silêncio...")
#         continue
#     # analise de movimento - n seria possivel usar so if e elif 
#     #  (conflitou mudança de posição e atirada de meloes no codigo passado)
#     if (fototirada[posicao - 1] == 'O') != (fototirada[posicao + 1] == 'O'):
#         if fototirada[posicao + 1] == 'O':
#             proximaPosicao = posicao + 1 
#         else:
#             proximaPosicao = posicao - 1
#         print(f"Correndo pro esconderijo {proximaPosicao}!")
#         posicao = proximaPosicao
#         continue

#     # se vou atirar melao
#     if fototirada[posicao] == 'O':
#         print("Tiro de Melão!!!")
#         meloesAtirados += 1
#         continue

# print(f"Vitória com {meloesAtirados} melões!")



'''
movimentosPossiveis = []
    if posicao > 0 and fototirada[posicao - 1] == 'O':  # Movimento para a esquerda
        movimentosPossiveis.append(posicao - 1)
    if posicao < len(fototirada) - 1 and fototirada[posicao + 1] == 'O':  # Movimento para a direita
        movimentosPossiveis.append(posicao + 1)
'''

s = input()
p =0 
meloes = 0
while 'X' in s:
    if s[p] == 'X':
        print('Silêncio...')
    elif (p+1<len(s) and s[p+1] == 'O') and ((p>0 and s[p-1]== 'X') or p == 0):
        print(f"Correndo pro esconderijo {p+1}!") 
        p+=1
    elif (p-1>= 0 and s[p-1] == 'O') and ((p+1 < len(s) and s[p+1] == 'X') or p == len(s)-1):
        p-=1
    else:
        meloes+=1
        print('Tiro de Melão!!!')
    s = input()
print (f"Vitória com {meloes} melões!")