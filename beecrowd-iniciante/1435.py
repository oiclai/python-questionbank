# O(n^2);
'''
while True:
    LinhaColuna=int(input())
    if LinhaColuna==0:
        break
    matriz=[[0 for j in range(LinhaColuna)] for i in range(LinhaColuna)]
    for i in range(LinhaColuna):
        for j in range(LinhaColuna):
            matriz[i][j] = 1 + min(i, j, LinhaColuna-1-i, LinhaColuna-1-j)

    for linha in matriz:
        print(" ".join(f"{num:3}" for num in linha))
    print() 
'''

'''
### solução mais rapida (praticamente metade do tempo) --> ainda O(n^2);
comp. temporal permanece O(n^2)
mas a comp. espacial é reduzida para O(1),
já que não armazenamos a matriz. *Pesquisar melhor sobre complexidade;
'''
while True:
# bloco usuario;
    LinhaColuna = int(input())
    if LinhaColuna == 0:
        break
# bloco criacao matriz;
    matriz = []
    for i in range(LinhaColuna):
        linha = [ # ficar mais flexivel quanto ao uso de list comprehension (thiago menciona mtt)
            1 + min(i, j, LinhaColuna - 1 - i, LinhaColuna - 1 - j)
            for j in range(LinhaColuna)
        ]
        matriz.append(linha)
# bloco impressao;
    for linha in matriz:
        print(" ".join(f"{num:3}" for num in linha))
    print()