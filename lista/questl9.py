'''Faça um Programa que leia um vetor A com 10 números inteiros,
calcule e mostre a soma dos quadrados dos elementos do vetor. '''
a = []
for n in range(1, 11):
    numero = int(input("Numero: "))
    numero *= numero
    a.append(numero)
soma = sum(a)
print(soma)
