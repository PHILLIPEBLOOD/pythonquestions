'''Altere o programa anterior, intercalando 3 vetores de 10 elementos cada. '''


def intercalados(a, b, c):
    d = []
    for n in range(1, 11):
        n -= 1
        d.append(a[n])
        d.append(b[n])
        d.append(c[n])
    return d


a = []
b = []
c = []
for n in range(1, 11):
    numero = int(input("Vetor 1: "))
    a.append(numero)
for n in range(1, 11):
    numero = int(input("Vetor 2: "))
    b.append(numero)
for n in range(1, 11):
    numero = int(input("Vetor 1: "))
    c.append(numero)
print(intercalados(a, b, c))
