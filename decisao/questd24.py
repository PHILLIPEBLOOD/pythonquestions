'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário
qual operação ele deseja realizar. O resultado da operação deve ser acompanhado
de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal. '''


def par_impar(number1, number2):
    tipo1 = tipo2 = "Impar"
    if(number1 % 2 == 0):
        tipo1 = "Par"
    if(number2 % 2 == 0):
        tipo2 = "Par"
    return tipo1, tipo2


def inteiro_decimal(number1, number2):
    tipo1 = tipo2 = "Decimal"
    if(round(number1) == number1):
        tipo1 = "Inteiro"
    if(round(number2) == number2):
        tipo2 = "Inteiro"
    return tipo1, tipo2


def positivo_negativo(number1, number2):
    tipo1 = tipo2 = "Positivo"
    if(number1 < 0):
        tipo1 = "Negativo"
    if(number2 < 0):
        tipo2 = "Negativo"
    return tipo1, tipo2


number1 = int(input("Numero "))
number2 = int(input("Numero "))
print("1-Par ou ímpar\n2-Positivo ou negativo\n3-Inteiro ou decimal.")
opcao = input("Opção 1, 2 ou 3: ")
if(opcao == "1"):
    tipo1, tipo2 = par_impar(number1, number2)
elif(opcao == "2"):
    tipo1, tipo2 = inteiro_decimal(number1, number2)
elif(opcao == "3"):
    tipo1, tipo2 = positivo_negativo(number1, number2)
print(number1, tipo1)
print(number2, tipo2)
