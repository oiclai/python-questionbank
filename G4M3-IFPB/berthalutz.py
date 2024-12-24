def senha(numeroVisor):
    visorEmString = str(numeroVisor); qtd_caract_visor = len(visorEmString); maxSoma = 0
    # me enrolei ate chegar aos dois 'for', atençao!!!!!
    for a in range(1, qtd_caract_visor-1): 
        for z in range(a+1, qtd_caract_visor): 
            parte_1 = int(visorEmString[:a]) 
            parte_2 = int(visorEmString[a:z]) 
            parte_3 = int(visorEmString[z:])
            soma = (parte_1 + parte_2 + parte_3)
            maxSoma = max(maxSoma, soma)
    return maxSoma

numeroVisor = int(input())
print(senha(numeroVisor))
