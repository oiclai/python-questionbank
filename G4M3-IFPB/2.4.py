listinha= []
cont = 0
for i in range(4):
    frase = input().strip()
    listinha.append(frase)
    if listinha[0][-2] + listinha[0][-1] == listinha[2][-2] + listinha[2][-1]:
        cont+=2
    elif listinha[1][-2] + listinha[1][-1] == listinha[3][-2] + listinha[3][-1]:
        cont+=2
print(cont)

# frase[1][-2] + frase[1][-1]
# == frase[3][-2] + frase[3][-1]