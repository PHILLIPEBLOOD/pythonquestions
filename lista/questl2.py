'''Faça um Programa que leia um vetor de 10 números reais e
mostre-os na ordem inversa. '''
reais = []
for n in range(1, 11):
    numero = float(input("Numero: "))
    reais.append(numero)
while n > 0:
    n -= 1
    print(reais[n])
