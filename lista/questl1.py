'''Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
'''
inteiros = []
for n in range(1, 6):
    numero = int(input("Numero: "))
    inteiros.append(numero)
    print(inteiros[n-1])
