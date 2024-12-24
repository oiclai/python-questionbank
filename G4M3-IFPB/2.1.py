# texto_criptografado = input()
# tamanho = len(texto_criptografado)
# for i in range(tamanho):
#     if letra[i + 1 % tamanho] == 'P' and letra[i + 2 % tamanho] == 'P':
# crip = input()
# while 'P' in crip:
#     crip = crip.replace('P', ' ')
#     for i in range(len(crip)):
#         if crip[i]==' ' and crip[i+1%len(crip)]==' ':
#             crip[i+1]='P'
            
# print(crip)


crip = input('')
cripo = ''
i = 0
while i < len(crip):
    if crip[i] == 'P' and crip[(i+1) % len(crip)] == 'P' and crip[(i+2) % len(crip)] == 'P':
        cripo += 'P'
        i +=2
    elif crip[i] == 'P':
        pass
    else:
        cripo += crip[i]
        cripo.replace('P','')
    i += 1
print(cripo)


# textonovo = texto_criptografado.replace('P', '')
# print(textonovo)