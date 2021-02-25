'''Faça um Programa que peça um número e informe
se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento.'''
number = float(input("Numero: "))
tipo = "Decimal"
if(round(number) == number):
    tipo = "Inteiro"
print(tipo)
