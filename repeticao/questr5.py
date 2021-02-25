'''Altere o programa anterior permitindo ao usuário informar as populações e
as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação. '''
a = int(input("Cidade A: "))
b = int(input("Cidade B: "))
crescimento_a = int(input("Taxa de crecimento ")) / 100
crescimento_b = int(input("Taxa de crescimento: ")) / 100
anos = 0
while(a > b):
    a = int(input("Cidade A: "))
    b = int(input("Cidade B: "))
    crescimento_a = float(input("Taxa de crescimento: ")) / 100
    crescimento_b = float(input("Taxa de crescimento: ")) / 100
while(a <= b):
    a *= 1 + crescimento_a
    b *= 1 + crescimento_b
    anos += 1
print(anos, "anos")
