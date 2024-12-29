n1,n2,n3,n4=map(int,input().split("."))
soma=n1+n2+n3+n4
if soma%8==0:
    print("BLOCK")
else:
    print("PASS")