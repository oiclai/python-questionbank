palavra=input().upper()
repeticoes={}
string='BCDEF'
letra_comandos=[]
for letra in palavra:
    if letra not in repeticoes:
        repeticoes[letra] =1
    else:
        repeticoes[letra]+=1
maior=0
for comandos in repeticoes:
    if repeticoes[comandos] > maior:
        maior= repeticoes[comandos]
for comando in string : 
    if repeticoes.get(comando, 0) == maior:
        letra_comandos.append(comando)
letra_comandos.sort()
print(letra_comandos[0])