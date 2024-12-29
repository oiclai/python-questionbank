n=int(input())
valores=[]
for i in range(n):
    num=int(input())
    valores.append(num)
if n<32:
    for j in range(n):
        print(valores[j])
else:
    for w in range(32):
        print(valores[w])