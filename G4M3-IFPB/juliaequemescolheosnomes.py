'''
n = int(input())
letra = []
for _ in range(n):
  line = input()
  if line[0] not in letra:
    letra.append(line[0])
print(len(letra))
'''
n = int(input())
lines = [input().strip() for _ in range(n)]
st = set()
for line in lines:
  st.add(line[0])
print(len(st))
