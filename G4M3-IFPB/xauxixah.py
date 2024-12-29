a,b=map(int,input().split(" "))
ab=a+b
div=1
for i in range(1,ab+1):
    if ab%i==0:
        div*=i
if div==ab:
    print("Xau")
else:
    print("Xi")