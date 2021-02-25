'''Faça um Programa que peça um número correspondente a um determinado ano e
em seguida informe se este ano é ou não bissexto.
'''
ano = int(input("Ano: "))
sexto = "Não bissexto"
if(ano % 4 == 0):
    sexto = "Bissexto"
print(sexto)
