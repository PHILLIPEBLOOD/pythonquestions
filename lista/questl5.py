'''Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os três vetores.
'''
inteiros = []
pares = []
impares = []
for n in range(1, 21):
    numero = int(input("Numero: "))
    inteiros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
for numero in inteiros:
    print(numero)
for par in pares:
    print(par)
for impar in impares:
    print(impar)
