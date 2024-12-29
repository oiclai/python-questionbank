n,e=map(int,input().split(" ")) #n= num de produtores & e=valor total esperado
totalmeloes=0
for i in range(n):
    meloes=int(input(""))
    if 1<=meloes<=9:
        totalmeloes+=meloes
if totalmeloes>=e:
    print("NADA PREOCUPANTE")
elif totalmeloes>=(e-5):
    print("POUCO PREOCUPANTE")
elif totalmeloes<(e-5):
    print("MUITO PREOCUPANTE")