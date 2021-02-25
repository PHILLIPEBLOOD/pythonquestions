'''Faça um Programa que leia três números
e mostre-os em ordem decrescente'''
number1 = int(input(""))
number2 = int(input(""))
number3 = int(input(""))
if(number2 > number1):
    number1, number2 = number2, number1
if(number3 > number2):
    number2, number3 = number3, number2
if(number2 > number1):
    number1, number2 = number2, number1
print(number1, number2, number3)
