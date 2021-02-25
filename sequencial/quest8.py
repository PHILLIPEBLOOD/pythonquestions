# Faça um Programa que pergunte 
# quanto você ganha por hora e 
# o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.
def salario(ganhohora, horastrabalhadas):
    return ganhohora * horastrabalhadas

ganhohora = int(input("Quanto você ganha por hora: "))
horastrabalhadas = int(input("Horas trabalhadas: "))
print ("Salario de", salario(ganhohora, horastrabalhadas), "R$")


