'''Faça um programa que leia 5 números e informe a soma e a média dos números.
'''
soma = 0
for n in range(1, 6):
    numero = int(input("Numero: "))
    soma += numero
media = soma / 5
print("Soma: ", soma)
print("Media: ", media)
