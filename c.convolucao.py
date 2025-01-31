linhaColuna = int(input())
matriz = []
for i in range(linhaColuna):
  linha = input().strip()
  matriz.append(linha)
matriz = matriz[::-1]
for b in range(linhaColuna):
  print(f'{matriz[b][::-1]:1}')
