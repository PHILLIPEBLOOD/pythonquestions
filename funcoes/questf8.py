'''Faça uma função que informe a quantidade de dígitos de um determinado número
inteiro informado. '''


def tamanho(numero):
    numero = str(numero)
    return len(numero)


numero = int(input("Numero: "))
print(tamanho(numero), "digitos")
