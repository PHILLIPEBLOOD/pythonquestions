"Faça um programa que leia 5 números e informe o maior número. "
maior = int(input("Digite um numero: "))
for n in range(1, 5):
    numero = int(input("Digite um numero: "))
    if(numero > maior):
        maior = numero
print("Maior", maior)
