numJogadores = int(input())
listaTotalSaque = []
listaTotalBloqueio = []
listaTotalAtaque = []
listaAcertoSaque = []
listaAcertoBloqueio = []
listaAcertoAtaque = []
# fazer com acumuladores tbm daria certo
for i in range(numJogadores):
    nomeJogador = input()
    tentativasTotais = input().split(" ")
    s,b,a = int(tentativasTotais[0]),int(tentativasTotais[1]),int(tentativasTotais[2])
    tentativasAcertadas = input().split(" ")
    s1,b1,a1 = int(tentativasAcertadas[0]),int(tentativasAcertadas[1]),int(tentativasAcertadas[2])
    listaTotalSaque.append(s)
    listaTotalBloqueio.append(b)
    listaTotalAtaque.append(a)
    listaAcertoSaque.append(s1)
    listaAcertoBloqueio.append(b1)
    listaAcertoAtaque.append(a1)
PorcentagemSaque=((sum(listaAcertoSaque)/sum(listaTotalSaque))*100)
PorcentagemBloqueio=((sum(listaAcertoBloqueio)/sum(listaTotalBloqueio))*100)
PorcentagemAtaque=((sum(listaAcertoAtaque)/sum(listaTotalAtaque))*100)
print(f"Pontos de Saque: {PorcentagemSaque:.2f} %.")
print(f"Pontos de Bloqueio: {PorcentagemBloqueio:.2f} %.")
print(f"Pontos de Ataque: {PorcentagemAtaque:.2f} %.")