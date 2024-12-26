import math
def operacao1 (numero:int):
    if numero>9999999:
        numero=9999999
    return f"{numero:.0f}"
def operacao2 (numero:int):
    op = math.log(numero, 2)
    if op>9999999:
        op=9999999
    return f"{op:.0f}"
def operacao3 (numero:int):
    op = math.sqrt(numero)
    if op>9999999:
        op=9999999
    return f"{op:.0f}"
def operacao4 (numero:int):
    op = numero * math.log(numero, 2)
    if op>9999999:
        op=9999999
    return f"{op:.0f}"
def operacao5 (numero:int):
    op = numero**2
    if op>9999999:
        op=9999999
    return f"{op:.0f}"
def operacao6 (numero:int):
    op = numero**3
    if op>9999999:
        op=9999999
    return f"{op:.0f}"
def operacao7 (numero:int):
    op = 2**numero
    if op>9999999:
        op=9999999
    return f"{op:.0f}"
def operacao8 (numero:int):
    op = math.factorial(numero)
    if op>9999999:
        op=9999999
    return f"{op:.0f}"

l, r = list(map(int, input().split()))
intervalo = [i for i in range(l, r + 1)]
op1, op2, op3, op4, op5, op6, op7, op8 = list(map(int, input().split()))
for j in intervalo:
    if op1 == 1:
        print(operacao1(j), end=" ")
    if op2 == 1:
        print(operacao2(j), end=" ")
    if op3 == 1:
        print(operacao3(j), end=" ")
    if op4 == 1:
        print(operacao4(j), end=" ")
    if op5 == 1:
        print(operacao5(j), end=" ")
    if op6 == 1:
        print(operacao6(j), end=" ")
    if op7 == 1:
        print(operacao7(j), end=" ")
    if op8 == 1:
        print(operacao8(j), end=" ")
    print()