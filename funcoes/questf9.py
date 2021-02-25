'''Reverso do número. Faça uma função que retorne o reverso de um número
inteiro informado. Por exemplo: 127 -> 721. '''
from questf8.py import tamanho


def reverso(numero):
    n = tamanho(numero) - 1
    numero = str(numero)
    inverso = ""
    while(n >= 0):
        inverso += numero[n]
    return inverso


numero = int(input("Numero: "))
print(reverso(numero))
