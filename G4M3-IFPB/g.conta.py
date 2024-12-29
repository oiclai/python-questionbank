SaldoAnterior=int(input(""))
ErroSaque=0
MaiorSaque=0
MaiorDeposito=0
total=SaldoAnterior
for i in range(1,8+1):
    movimentacao=int(input(""))
    if movimentacao>MaiorDeposito:
        MaiorDeposito=movimentacao
    if movimentacao<(-total):
        ErroSaque+=1
    else:
        total+=movimentacao
        if movimentacao<MaiorSaque:
            MaiorSaque=movimentacao
if MaiorSaque==0:
    print("SEM MOVIMENTO DE SAQUE")
else:
    print(f"Maior saque: {-MaiorSaque:.2f}")
if MaiorDeposito==0:
    print("SEM MOVIMENTO DE DEPOSITO")
else:
    print(f"Maior deposito: {MaiorDeposito:.2f}")
print(f"Erros de saque: {ErroSaque}")
print(f"Saldo final: R$ {total:.2f}")