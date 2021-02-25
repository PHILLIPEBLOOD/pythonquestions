'''Foram anotadas as idades e alturas de 30 alunos.
 Faça um Programa que determine quantos alunos com mais de 13 anos possuem
 altura inferior à média de altura desses alunos.
'''
idades = []
alturas = []
for n in range(0, 30):
    idade = int(input("Idade: "))
    altura = float(input("Altura: "))
    idades.append(idade)
    alturas.append(altura)
media = sum(alturas) / 30
cont = 0
for n in range(0, 30):
    if idades[n] > 13 and alturas[n] < media:
        cont += 1
