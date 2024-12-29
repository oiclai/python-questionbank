'''
A entrada possui apenas uma linha contendo a string com as cores do semáforo que o drone capturou.

Considere que a string possui no mínimo 3 e no máximo 100 caracteres.

Considere que a string é composta apenas pelas letras Y (Amarelo) R (Vermelho) e G (Verde). Todas maiúsculas.

Saída
Seu programa deve imprimir YES caso a sequência de cores esteja correta e NO caso contrário.

Atenção com as letras maiúsculas e minúsculas! Neste problema, a solução deve ser impressa toda em maiúsculas.
'''
tamanho = int(input())
semaforo = input()
sequenciaValida = True
# YRG
for i in range(tamanho - 1): # tentativa de resolver o problema de index out of range
    if semaforo[i] == 'R' and semaforo[i + 1] != 'G':
        sequenciaValida = False
        break
    if semaforo[i] == 'Y' and semaforo[i + 1] != 'R':
        sequenciaValida = False
        break
    if semaforo[i] == 'G' and semaforo[i + 1] != 'Y':
        sequenciaValida = False
        break

print("YES" if sequenciaValida else "NO") # amando usar isso q daniel ensinou