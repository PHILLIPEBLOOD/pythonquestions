'''Faça um Programa que leia um vetor de 10 caracteres, e diga quantas
consoantes foram lidas. Imprima as consoantes. '''


def verifica_consoate(char):
    vogais = ['a', 'e', 'i', 'o', 'u']
    if char in vogais:
        return False
    return True


caracteres = []
for n in range(1, 11):
    char = input("Letra; ")
    caracteres.append(char)
for char in caracteres:
    if(verifica_consoate(char)):
        print(char)
