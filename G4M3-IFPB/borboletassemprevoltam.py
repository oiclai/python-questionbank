n=int(input())
string=input()
novastring= string[:n]
tem=0
for letra in novastring:
    if letra=='B':
        tem+=1
if tem!=0:
    print('Borboletas Sempre Voltam')
else:
    print('Nem Sempre')