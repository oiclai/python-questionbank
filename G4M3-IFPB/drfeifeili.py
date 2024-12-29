linha=input("")
for i in range(len(linha)):
    if i < len(linha)-1:
        if linha[i] == "o" and linha[i+1] == "O":
            print("YES")
            break
        elif linha[i] == "O" and linha[i+1] == "o":
            print("YES")
            break
    else:
        print("NO")