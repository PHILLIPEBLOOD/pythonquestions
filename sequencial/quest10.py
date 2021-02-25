# Faça um Programa que peça a temperatura em graus Celsius, 
# transforme e mostre em graus Fahrenheit.
def convertertemperatura(C):
    return (C * 9) / 5 + 32
    
C = int(input("Celsius: "))
print(convertertemperatura(C), "farenrait")
