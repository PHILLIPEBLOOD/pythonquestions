'''
Faça um programa que peça 10 números inteiros, calcule e mostre a
quantidade de números pares e a quantidade de números impares.
'''
par = 0
impar = 0
for n in range(1, 11):
    numero = int(input("Digite: "))
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
print("Pares: ", par)
print("Impares: ", impar)
