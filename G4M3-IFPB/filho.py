rep=int(input())
for i in range(rep):
    poder1=0
    poder2=0
    nomes=input().split(" ")
    nome1=nomes[0]
    nome2=nomes[1]
    for j in nome1:
        if j=="a":
            poder1+=1
        if j=="e":
            poder1+=2
        if j=="i":
            poder1+=3
        if j=="o":
            poder1+=4
        if j=="u":
            poder1+=5
        if j=="y":
            poder1+=100
    for j in nome2:
        if j=="a":
            poder2+=1
        if j=="e":
            poder2+=2
        if j=="i":
            poder2+=3
        if j=="o":
            poder2+=4
        if j=="u":
            poder2+=5
        if j=="y":
            poder2+=100
    if poder1>poder2:
        print(nome1)
    elif poder2>poder1:
        print(nome2)
    else:
        print("naruto")