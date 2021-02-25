# Faça um Programa que calcule a área de um quadrado, 
# em seguida mostre o dobro desta área para o usuário
def dobroarea(lado):
    return 2 * (lado * lado)

lado = int(input("Lado: "))
print(dobroarea(lado))

