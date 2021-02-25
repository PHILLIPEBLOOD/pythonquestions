'''Faça um Programa que leia três números e mostre o maior deles. '''
number1 = int(input())
number2 = int(input())
number3 = int(input())


def func_maior(number_1, number_2, number_3):
    maior = number_1
    if number_2 > maior:
        maior = number_2
    if number_3 > maior:
        maior = number_3
    return maior


print(func_maior(number1, number2, number3))
