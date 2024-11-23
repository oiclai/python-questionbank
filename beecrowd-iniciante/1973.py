numeroDeEstrelas= int(input())
carneirosRoubados = 0
carneiros = list(map(int, input().split()))
indicesEstrelas = [i for i in range(numeroDeEstrelas)]
while True:
        if carneiros[0] % 2 == 0:
            carneirosRoubados += 1
            break
        else:
            for i in range(indicesEstrelas):
                if carneiros[i] % 2 == 0:
                     
                elif carneiros[i] % 2 != 0:



# carneiros = map(int, input().split())


# for i in range(1,len(carneiros)+1):


# carneiros = dict(zip(map(int, input("Digite números separados por espaço: ").split()), map(int, input("Digite os valores para cada chave separados por espaço: ").split())))
# print(carneiros)
