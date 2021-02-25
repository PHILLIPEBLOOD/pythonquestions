'''Valida e corrige número de telefone. Faça um programa que leia um número de
telefone, e corrija o número no caso deste conter somente 7 dígitos,
acrescentando o '3' na frente. O usuário pode informar o número com ou sem o
traço separador. '''
telefone = input("Digite seu número: ")
printar = telefone
if(("-" in telefone and len(telefone) == 8) or len(telefone) == 7):
    printar = telefone + "3"
print(printar)
