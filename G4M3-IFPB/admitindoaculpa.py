rep = int(input())
for i in range(rep):
    numero = input()
    a, b, c = int(numero[0]), int(numero[1]), int(numero[2])
    tentativa1 = a + (b*10 + c)  # a + bc
    tentativa2 = (a*10 + b) + c  # ab + c
    print(max(tentativa1, tentativa2))

    

