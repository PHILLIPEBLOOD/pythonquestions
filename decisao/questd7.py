'''Faça um Programa que leia três números e mostre o maior e o menor deles.'''


def func_maior(number_1, number_2, number_3):
    maior = number_1
    if number_2 > maior:
        maior = number_2
    if number_3 > maior:
        maior = number_3
    return maior


number_1 = int(input(""))
number_2 = int(input(""))
number_3 = int(input(""))
maior = func_maior(number_1, number_2, number_3)


def func_menor(number1, number2, number3):
    menor = number1
    if number2 < menor:
        menor = number2
    if number3 < menor:
        menor = number3
    return menor


menor = func_menor(number_1, number_2, number_3)
print(maior)
print(menor)
