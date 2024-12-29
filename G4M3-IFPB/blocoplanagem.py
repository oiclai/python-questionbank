vetorblocos=[]
menor=100
totalAteMenor=0
for i in range (5):
    x=int(input(""))
    if x<menor:
        menor=x
    vetorblocos.append(x)
for j in vetorblocos:
    totalAteMenor+=(j-menor)
print(totalAteMenor)