digitos = int(input())
numero = input()
alice = []
bulba = []
for i in range(digitos):
    if i % 2 == 0:
        alice.append('0')
        bulba.append(numero[i])
    else:
        alice.append(numero[i])
        bulba.append('0')

print(''.join(alice))
print(''.join(bulba))        
