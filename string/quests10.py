'''Número por extenso. Escreva um programa que solicite ao usuário a digitação
de um número até 99 e imprima-o na tela por extenso. '''


def numero_extenso(numero):
    dezenas = {
        2: "vinte",
        3: "trita",
        4: "quarenta",
        5: "cinquenta",
        6: "sessenta",
        7: "setenta",
        8: "oitenta",
        9: "noventa"
    }
    unidades = {
        1: "um",
        2: "dois",
        3: "três",
        4: "quatro",
        5: "cinco",
        6: "seis",
        7: "sete",
        8: "oito",
        9: "nove",
        10: "dez",
        11: "onze",
        12: "duze",
        13: "treze",
        14: "quatorze",
        15: "quinze",
        16: "dezesseis",
        17: "dezessete",
        18: "dezoito",
        19: "dezenove",
    }
    deze = int(numero / 10)
    numero = numero - (deze * 10)
    uni = int(numero % 20)
    texto = ""
    try:
        texto += dezenas[deze]
        texto += " e " + unidades[uni]
    except TypeError:
        texto += unidades[uni]
    return texto


numero = int(input())
texto = ""
if numero < 100:
    texto = numero_extenso(numero)
print(texto)
