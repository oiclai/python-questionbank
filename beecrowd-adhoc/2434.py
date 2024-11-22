numeros =input().split(" ")
dias = int(numeros[0])
SaldoInicial = int(numeros[1])
menor=SaldoInicial
for i in range(dias):
    m=int(input())
    SaldoInicial+=(m)
    if SaldoInicial<menor:
        menor=SaldoInicial
print(menor)