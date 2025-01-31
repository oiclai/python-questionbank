soma = 0
n = int(input())
for i in range(1, (n//2)+1):
  if n%i == 0:
    soma +=1
if soma > n:
  print("SIM")
elif soma <= n:
  print("NAO")
