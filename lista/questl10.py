'''Faça um Programa que leia dois vetores com 10 elementos cada. Gere um
terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos
elementos intercalados dos dois outros vetores. '''


def intercalados(a, b):
    c = []
    for n in range(1, 11):
        n -= 1
        c.append(a[n])
        c.append(b[n])
    return c


a = []
b = []
for n in range(1, 11):
    numero = int(input("Vetor 1: "))
    a.append(numero)
for n in range(1, 11):
    numero = int(input("Vetor 2: "))
    b.append(numero)
print(intercalados(a, b))
