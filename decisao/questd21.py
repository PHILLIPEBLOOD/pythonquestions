''' Faça um Programa para um caixa eletrônico. O programa deverá perguntar
ao usuário a valor do saque e depois informar quantas notas de cada valor
serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se
preocupar com a quantidade de notas existentes na máquina.
Exemplo 1:
Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2:
Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1. '''


def quantidade_extenso(notas, valor_nota):
    quant_notas = {
        1: "uma",
        2: "duas",
        3: "três",
        4: "quatro",
        5: "cinco",
        6: "seis",
    }
    if notas <= 0:
        return ""
    return ", " + quant_notas[notas] + " notas de " + str(valor_nota)


def quant_nota(valor_restante, valor_nota):
    notas = int(valor_restante/valor_nota)
    if(notas < 0):
        return 0
    return notas


def quantidade_notas(valor_saque):
    nota_100 = quant_nota(valor_saque, 100)
    valor_saque = valor_saque - (nota_100 * 100)
    notas_saque = quantidade_extenso(nota_100, 100)
    nota_50 = int(valor_saque/50)
    valor_saque = valor_saque - (nota_50 * 50)
    notas_saque = notas_saque + quantidade_extenso(nota_50, 50)
    nota_10 = int(valor_saque/10)
    valor_saque = valor_saque - (nota_10 * 10)
    notas_saque = notas_saque + quantidade_extenso(nota_10, 10)
    nota_5 = int(valor_saque/5)
    valor_saque = valor_saque - (nota_5 * 5)
    notas_saque = notas_saque + quantidade_extenso(nota_5, 5)
    nota_1 = int(valor_saque/1)
    return notas_saque + quantidade_extenso(nota_1, 1)


valor_saque = int(input("Valor do saque: "))
saque = "Valor invalido!"
if(valor_saque >= 10):
    saque = quantidade_notas(valor_saque)
print("Para sacar a quantia de ", valor_saque, "O programa fornece", saque)
