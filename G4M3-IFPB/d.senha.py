'''
Uma senha para ser considerada forte deve possuir:

Todos os símbolos distintos, ou seja, não repetem (são diferentes);
10 caracteres, no mínimo;
02 letras minúsculas, no mínimo;
02 letras maiúsculas, no mínimo;
02 números, no mínimo;
02 caracteres especiais, no mínimo.
Escreva um programa para ler uma senha e informar se esta é uma senha forte ou não.
'''
def senha_forte(senha: str)-> str:
    maiusculas ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    minusculas = 'abcdefghijklmnopqrstuvwxyz'
    numeros = '0123456789'
    especiais = '!@#$%^&*()-_=+[]{}|;:,.<>/?'
    set_senha = set(senha)
    qtd_maiusculas = qtd_minusculas = qtd_numeros = qtd_especiais = 0
    if len(senha) < 10 or len(senha) != len(set_senha):
        return 'N'
    for caractere in senha:
        if caractere in maiusculas:
            qtd_maiusculas += 1
        if caractere in minusculas:
            qtd_minusculas += 1
        if caractere in numeros:
            qtd_numeros += 1
        if caractere in especiais:
            qtd_especiais += 1
    if qtd_maiusculas >= 2 and qtd_minusculas >= 2 and qtd_numeros >= 2 and qtd_especiais >= 2:
        return 'S'
    return 'N'
senha = input().strip()
print(senha_forte(senha))