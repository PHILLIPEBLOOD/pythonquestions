'''Data por extenso. Faça um programa que solicite a data de nascimento
(dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.
Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.
'''
from def_questf import mes_extenso
data = input("Data: ")
print("Você nasceu em ", mes_extenso(data))
