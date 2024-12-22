qtdLinhas = int(input())
alfabeto = "abcdefghijklmnopqrstuvwxyz"
letrasNaoUsadas= []
letrasUsadas = set()
for i in range(qtdLinhas):
    frase = input().lower()
    for letra in frase:
        if letra in alfabeto:
            letrasUsadas.add(letra)
for letra in alfabeto:
    if letra not in letrasUsadas:
        letrasNaoUsadas.append(letra)
print("".join(letrasNaoUsadas))



'''
12
Alma luz
Minha alma tem o peso da luz
Tem o peso da musica
Tem o peso da palavra nunca dita,
Prestes quem sabe a ser dita
Tem o peso de uma lembranca
Tem o peso de uma saudade
Tem o peso de um olhar
Pesa como pesa uma ausencia
E a lagrima que nao chorou
Tem o imaterial peso de uma solidao
No meio de outros


Saida
fjkwxy
'''