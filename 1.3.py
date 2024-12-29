n,r=map(int,input().split(" "))
lista=input().split(" ")
lista=map(int, lista)
for _ in lista:
    if _ <=r:
        print("1")
    else:
        print("0")