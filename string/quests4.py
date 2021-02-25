'''Nome na vertical em escada. Modifique o programa anterior de forma a mostrar
o nome em formato de escada.
F
FU
FUL
FULA
FULAN
FULANO '''
nome = input("Nome: ")
i = len(nome)
a = 1
while a <= i:
    print(nome[0:a])
    a += 1
