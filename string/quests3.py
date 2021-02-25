'''Nome na vertical. Faça um programa que solicite o nome do usuário e
imprima-o na vertical.
F
U
L
A
N
O
'''
nome = input("Nome: ")
i = len(nome) - 1
a = 0
while a <= i:
    print(nome[a])
    a += 1
print()
