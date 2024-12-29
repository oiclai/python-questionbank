while True:
  try:
    numero = int(input())
    matriz = []
    for i in range(numero):
      linha = [
        2 if i + j == numero - 1 else 1 if i == j else 3 # novidade
        for j in range(numero)
      ]
      matriz.append(linha)
    for linha in matriz:
      print("".join(f"{num}" for num in linha))
  except EOFError:
    break
