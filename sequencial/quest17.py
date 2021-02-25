'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
 é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas
e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
considere latas cheias.
'''
import math


def lata_maior(areapintada):
    latas = math.ceil(areapintada/108)
    return latas


def lata_menor(area_pintada):
    latas_menor = math.ceil(area_pintada/21.6)
    return latas_menor


def latamix(area_pintada):
    latas = int(area_pintada/108)
    metros_restantes = area_pintada - (latas*108)
    latas_menor = lata_menor(metros_restantes)
    return latas, latas_menor


area_pintada = int(input("Area pintada: "))
latas,  latas_menor = latamix(area_pintada)
print(lata_maior(area_pintada), "latas grandes")
print(lata_menor(area_pintada), "latas menores")
print("Mix de", latas, "latas grandes", latas_menor, "latas menores")
