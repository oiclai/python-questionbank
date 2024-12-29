qntd=0
for i in range(1,32+1):
    tempo=input().split(":")
    hora=int(tempo[0])
    min=int(tempo[1])
    seg=int(tempo[2])
    if 22<=hora<=23 or 00<=hora<6:
        if 0<=min<=59:
            if 0<=seg<=59:
                qntd+=1
print(qntd)