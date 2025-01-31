rep, saldoInicial = map(int, input(). split())
comprados, gastos = 0
for i in range(rep):
  string = input()
  if string == '+':
    valor = int(string[2::])
    saldoInicial += valor
  else:
    valor = int(string[2::])
    if saldoInicial >= valor:
      saldoInicial-= valor
      gasto += valor
      comprados += 1
print(f'{comprados} {gasto:.0f} {saldoInicial:.0f}')
