'''Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo
delas seguido do seu comprimento. Informe também se as duas strings possuem o
mesmo comprimento e são iguais ou diferentes no conteúdo.
Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
'''
string1 = input()
string2 = input()
igualdade = "As duas strings possuem conteúdo diferente."
if string1 == string2:
    igualdade = "As duas strings possuem conteúdo igual."
tam1 = len(string1)
tam2 = len(string2)
string1 += str(tam1)
string2 += str(tam2)
tamanho = "As duas strings são de tamanhos diferentes."
if tam1 == tam2:
    tamanho = "As duas strings são de tamanhos iguais."
print(string1)
print(string2)
print(tamanho)
print(igualdade)
