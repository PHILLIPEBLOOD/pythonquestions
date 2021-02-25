# Faça um Programa que peça 2 números inteiros e 
# um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.
def produto(number1, number2):
    return (number1 * 2) * (number2 / 2)
    

def soma(number1, numberreal):
    return (number1 * 3) + numberreal
    

def elevado(numberreal):
    return numberreal ** 3

number1 = int(input("Inteiro: "))
number2 = int(input("Inteiro: "))
numberreal = float(input("Real: "))
print(produto(number1, number2))
print(soma(number1, numberreal))
print(elevado(numberreal))