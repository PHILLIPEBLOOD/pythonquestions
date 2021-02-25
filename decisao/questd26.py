'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
    Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros,
desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma:
A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do
litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''


def descontado(litros_vendidos):
    porcentagem_descontado = 0.97
    if(litros_vendidos > 20):
        return 0.94
    return porcentagem_descontado


litros_vendidos = int(input("Litros Vendidos: "))
tipo_combustivel = input("Tipo: ")
litro_preco = 2.5
if(tipo_combustivel == "A"):
    litro_preco = 1.9
total = (litro_preco * litros_vendidos) * descontado(litros_vendidos)
print(total)
