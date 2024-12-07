while True:
    LinhaColuna = int(input())
    if LinhaColuna == 0:
        break
    teste=1
    matriz = [
        [1 + (i - j) if i <= j else 0 for j in range(LinhaColuna)] 
        for i in range(LinhaColuna)
    ]

    for i in range(1, LinhaColuna):
        for j in range(i):  
            matriz[i][j] = matriz[j][i]  

    for linha in matriz:
        print(" ".join(f"{num:3}" for num in linha))
    print()
