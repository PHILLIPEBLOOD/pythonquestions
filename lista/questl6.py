'''Faça um Programa que peça as quatro notas de 10 alunos,
calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0. '''
medias = []
for n in range(1, 11):
    nota1 = float(input("Nota: "))
    nota2 = float(input("Nota: "))
    nota3 = float(input("Nota: "))
    nota4 = float(input("Nota: "))
    media_aluno = (nota1 + nota2 + nota3 + nota4) / 4
    medias.append(media_aluno)
cont_alunos = 0
for media_aluno in medias:
    if(media_aluno >= 7):
        cont_alunos += 1
print(cont_alunos)
