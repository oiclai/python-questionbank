s, k = map(int, input().split())
palindromo = input()
string = palindromo
for i in range(k):
  if s == 1:
    break
  string = string[::-1]
if string == palindromo:
  print("SIM")
else:
  print("NAO")
