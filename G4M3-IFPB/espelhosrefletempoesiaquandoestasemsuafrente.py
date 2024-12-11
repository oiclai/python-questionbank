'''
n = int(input())
linhalista = []
for _ in range (n):
  linha = list(input())
  linhanova = linha[::-1]
  linhalista.append(linhanova)
  listalegal = linhalista[::-1]
for linhanova in listalegal:
  print("".join(linhanova))
'''
n = int(input())
a = [input().strip() for _ in range(n)]
for i in reversed(a):
    print(i[::-1])