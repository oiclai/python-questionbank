n = int(input())
letra = []
conte = 0
for _ in range(n):
  line = input()
  if line[0] not in letra:
    letra.append(line[0])
print(len(letra))
