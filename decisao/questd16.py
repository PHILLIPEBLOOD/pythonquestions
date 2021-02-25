'''Faça um programa que calcule as raízes de uma equação do segundo grau, na
forma ax + bx + c. O programa deverá pedir os valores de a, b e c e fazer as
consistências, informando ao usuário nas seguintes situações: Se o usuário
informar o valor de A igual a zero, a equação não é do segundo grau
e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais.
Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
informe-a ao usuário;
Se o delta for positivo,
a equação possui duas raiz reais; informe-as ao usuário;
'''
import math
a = int(input("Digite a: "))
b = int(input("Digite b: "))
c = int(input("Digite c: "))
delta = (b ** 2) - (4 * a * c)
try:
    raizdelta = math.sqrt(delta)
    if(raizdelta == 0):
        raiz1 = (-b) / (2 * a)
        raizes = "A equação possui uma raiz\n" + str(raiz1)
    elif(raizdelta > 0):
        raiz1 = (-b) + raizdelta
        raiz2 = (-b) - raizdelta
        raizes = "A equação possui duas raizesz\n" + str(raiz1) + "\n" +\
            str(raiz2)
    print(raizes)
except ValueError:
    print("A equação não possui raizes")
