times,problemas=map(int,input().split(" "))
lista=input().split(" ")
vetorlista=map(int, lista)
baloesfaltosos=0
for i in vetorlista:
    if i < problemas:
        baloesfaltosos+=(problemas-i)
print(baloesfaltosos)