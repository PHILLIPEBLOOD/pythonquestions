#Tendo como dado de entrada a altura (h) de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
h = float(input("Altura: "))
sexo = input("Sexo: ")
if (sexo == "m"):
    print("Para homens:", (72.7*h) - 58)
elif (sexo == "f"):
    print("Para mulheres:", (62.1*h) - 44.7)
else:
    print("Escreva certo")
