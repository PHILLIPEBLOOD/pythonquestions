'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
informar se os valores podem ser um triângulo. Indique, caso os lados formem
um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior
que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
'''
lado1 = int(input("Lado do triangulo: "))
lado2 = int(input("Lado do triangulo: "))
lado3 = int(input("Lado do triangulo: "))
triangulo = "Isósceles"
if(lado1 == lado2 == lado3):
    triangulo = "Equilátero"
elif(lado1 != lado2 != lado3):
    triangulo = "Escaleno"
print(triangulo)
