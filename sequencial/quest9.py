# Faça um Programa que peça a temperatura em graus Fahrenheit, 
# transforme e mostre a temperatura em graus Celsius.
def convertertemperatura(F):
    return 5 * ((F-32) / 9)

F = int(input("Fahrenheit: "))
print(convertertemperatura(F), "graus celsius")

