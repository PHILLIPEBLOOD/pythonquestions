'''Faça um programa para uma loja de tintas.
 O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta
a serem compradas e o preço total. '''
import math
areapintada = int(input("Area pintada: "))
latas = math.ceil(areapintada/54)     # 3*18 = 54
custo = latas * 80
print(latas, "latas de tinta")
print(custo, "R$")

