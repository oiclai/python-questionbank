def calculoMaxArea(moedas: int) -> int:
    base = moedas // 2
    altura = moedas - base
    return (2 ** base) * (2 ** altura) 
moedas = int(input())
print(calculoMaxArea(moedas))

