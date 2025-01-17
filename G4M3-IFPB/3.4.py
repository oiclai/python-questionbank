fila = []
while True:
    nome = input()
    if nome == 'FIM':
        break
    elif nome == 'PROXIMO':
        if fila: # n ta vazia
            print(f"PROXIMO: {fila[0]}")
            fila.pop(0)
    else:
        fila.append(nome)
        if fila:
            print("FILA:", " ".join(fila))