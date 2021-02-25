'''Faça um Programa que peça um número inteiro e determine se ele
é par ou impar. Dica: utilize o operador módulo (resto da divisão). '''
number = int(input())
tipo = "impar"
if(number % 2 == 0):
    tipo = "par"
print("O número é", tipo)
