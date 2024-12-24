a = int(input())
cont = 0     
for _ in range(a):
    frase=(input()).lower()
    if 'fada' in frase:
        cont+=1
print(cont)