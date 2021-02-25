'''Verificação de CPF. Desenvolva um programa que solicite a digitação de um
número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou
inválido através da validação dos dígitos verificadores e dos caracteres de
formatação. '''
cpf = input()
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
remover = [".", "-"]
try:
    for n in range(3, 15, 3):
        if n < 10 and cpf[n] == remover[0]:
            cpf = cpf[0:n] + cpf[n+1:]
        else:
            print(cpf[n])
            a = n + 1
            cpf = cpf[0:n] + cpf[a:]
    print(", ", cpf)
    c = int(cpf)
    if c >= 100000000:
        print("Número Valido!")
    else:
        print("Valor Invalido!")
except TypeError:
    print("Número Invalido!")
