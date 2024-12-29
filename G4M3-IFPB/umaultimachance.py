n=int(input(""))
ultimo=2*n
if n%2==0:
    for i in range(n+1,ultimo+1,2):
        print(i)
else:
    for i in range(n,ultimo+1,2):
        print(i)