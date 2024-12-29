cont=0
doacoes=0
while True:
    n=float(input(""))
    doacoes+=1
    cont+=n
    if cont>=10000:
        break
valorextra=cont-10000
print(f"Total arrecadado: R$ {cont:.2f}")
print(f"Doacoes recebidas: {doacoes}")
print(f"Valor extra arrecadado: R$ {valorextra:.2f}")