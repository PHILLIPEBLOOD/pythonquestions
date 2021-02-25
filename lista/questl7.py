'''Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma,
a multiplicação e os números. '''
inteiros = []
for n in range(1, 6):
    numero = int(input("Numero: "))
    inteiros.append(numero)
soma = 0
multiplica = 1
for numero in inteiros:
    soma += numero
    multiplica *= numero
    print(numero, end=" ")
print("Soma:", soma)
print("Multiplicação", multiplica)
