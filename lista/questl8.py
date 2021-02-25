'''Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada
informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa
a ordem lida. '''
idades = []
alturas = []
for n in range(1, 6):
    pessoa_idade = int(input("Idade: "))
    pessoa_altura = int(input("Altura: "))
    idades.append(pessoa_idade)
    alturas.append(pessoa_altura)
while n > 0:
    n -= 1
    print(idades[n], end=" ")
    print(alturas[n])
