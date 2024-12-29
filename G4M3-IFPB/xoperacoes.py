import math

def operacao1(numero: int):
    if numero > 9999999:
        numero = 9999999
    return str(math.floor(numero))

def operacao2(numero: int):
    op = math.log(numero, 2)
    if op > 9999999:
        op = 9999999
    return str(math.floor(op))

def operacao3(numero: int):
    op = math.sqrt(numero)
    if op > 9999999:
        op = 9999999
    return str(math.floor(op))

def operacao4(numero: int):
    op = numero * math.log(numero, 2)
    if op > 9999999:
        op = 9999999
    return str(math.floor(op))

def operacao5(numero: int):
    op = numero**2
    if op > 9999999:
        op = 9999999
    return str(math.floor(op))

def operacao6(numero: int):
    op = numero**3
    if op > 9999999:
        op = 9999999
    return str(math.floor(op))

def operacao7(numero: int):
    op = 2**numero
    if op > 9999999:
        op = 9999999
    return str(math.floor(op))

def operacao8(numero: int):
    op = math.factorial(numero)
    if op > 9999999:
        op = 9999999
    return str(math.floor(op))

l, r = list(map(int, input().split()))
intervalo = [i for i in range(l, r + 1)]
op1, op2, op3, op4, op5, op6, op7, op8 = list(map(int, input().split()))

for j in intervalo:
    resultados = []
    if op1 == 1:
        resultados.append(operacao1(j))
    if op2 == 1:
        resultados.append(operacao2(j))
    if op3 == 1:
        resultados.append(operacao3(j))
    if op4 == 1:
        resultados.append(operacao4(j))
    if op5 == 1:
        resultados.append(operacao5(j))
    if op6 == 1:
        resultados.append(operacao6(j))
    if op7 == 1:
        resultados.append(operacao7(j))
    if op8 == 1:
        resultados.append(operacao8(j))
    
    print(" ".join(resultados))
