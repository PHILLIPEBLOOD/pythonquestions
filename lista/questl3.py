'''Faça um Programa que leia 4 notas, mostre as notas e a média na tela. '''
notas = []
for n in range(1, 5):
    nota = float(input("Nota: "))
    notas.append(nota)
media = sum(notas) / n
print("Media: ", media)
