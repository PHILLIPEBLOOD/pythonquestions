'''Faça um Programa que peça um valor e
mostre na tela se o valor é positivo ou negativo'''


def posinega(number1):
    return number1 >= 0


number1 = int(input("Numero: "))
valor = "Negativo"
if(posinega(number1)):
    valor = "Positivo"

print(valor)
