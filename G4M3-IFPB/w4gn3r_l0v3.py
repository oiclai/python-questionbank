def checagem(string):
    num='0123456789'
    for elem in string:
        if elem in num:
            return True
    return False
n=int(input())
string=input()
stringnova=string[:n]
if (checagem(stringnova)):
    print(f'{stringnova} YES')
else:
    print(f'{stringnova} NO')