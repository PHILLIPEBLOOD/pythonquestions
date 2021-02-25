'''Faça um programa que receba dois números inteiros e gere os números inteiros
que estão no intervalo compreendido por eles.
'''
numero_1 = int(input("Numero: "))
numero_2 = int(input("Numero: "))
for n in range(numero_1+1, numero_2):
    print(n)
