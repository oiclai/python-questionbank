rodadas = int(input())
andressa =  bianca = 0
relacao_cartaValor = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'J':10,'Q':10,'K':10, 'X':10, 'C':999, 'A':0}
for i in range(rodadas):
    carta=input()
    if i % 2 == 0:
        if carta == 'C':
            andressa += relacao_cartaValor['C']
            break
        elif carta == 'A':
            andressa = 0
        andressa+=relacao_cartaValor[carta]
    else:
        if carta == 'C':
            bianca += relacao_cartaValor['C']
            break
        elif carta == 'A':
            bianca = 0
        bianca+=relacao_cartaValor[carta]
if bianca > andressa:
    print('BIANCA')
elif bianca < andressa:
    print('ANDRESSA')
else:
    print('EMPATE')
    