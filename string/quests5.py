'''Nome na vertical em escada invertida. Altere o programa anterior de modo
que a escada seja invertida.
FULANO
FULAN
FULA
FUL
FU
F '''
nome = input("Nome: ")
i = len(nome)
a = 1
while a <= i:
    print(nome[0:i])
    i -= 1
