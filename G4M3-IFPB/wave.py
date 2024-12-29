string=input().lower() # string minuscula
for i in range(len(string)): # repetições pela quantidade de letras da palavra
	print(string[0:i]+string[i].upper()+string[i+1:])