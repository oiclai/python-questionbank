tamanhoPopulacao = int(input()) # defender meloes
contadorMeloes = 0
contadorGoblin = 0
while True:
    hordaGoblinsAtaques, qtdMeloes, qtdGoblin = list(map(int, input().split()))
    if hordaGoblinsAtaques == 0 and qtdMeloes == 0 and qtdGoblin == 0:
        break
    if hordaGoblinsAtaques>tamanhoPopulacao:
        contadorMeloes += qtdMeloes
        contadorGoblin += qtdGoblin

    print(f'Meloes roubados: {contadorMeloes}\nGoblins resgatados: {contadorGoblin}\n---')
