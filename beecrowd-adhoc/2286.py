controlePartidas = 1; 
while True:
    numeroDePartidas = int(input()); # -> numero de partidas do jogo par ou impar
    if numeroDePartidas == 0:
        break;
    nomeJogadorPar = input();
    nomeJogadorImpar = input();
    print(f'Teste {controlePartidas}');
    for i in range(1, numeroDePartidas+1):
        numeros = input().split();
        jogadorPar = int(numeros[0]);
        jogadorImpar = int(numeros[1]);
        if (jogadorPar + jogadorImpar) % 2 == 0:
            print(nomeJogadorPar);
        else:
            print(nomeJogadorImpar);
    print();
    controlePartidas += 1;