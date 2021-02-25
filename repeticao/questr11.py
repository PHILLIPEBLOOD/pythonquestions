'''Altere o programa anterior para mostrar no final a soma dos números. '''
numero_1 = int(input("Numero: "))
numero_2 = int(input("Numero: "))
soma = 0
for n in range(numero_1+1, numero_2):
    print(n)
    soma += n
print("Soma", soma)
