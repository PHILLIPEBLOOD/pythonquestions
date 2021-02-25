'''Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
(em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. '''


def valor_pago(morango_kg, maca_kg):
    kilos = maca_kg + morango_kg
    morango_preco = 2.5
    maca_preco = 1.8
    porcent = 1.0
    if(morango_kg > 5):
        morango_preco = 2.2
    if(maca_kg > 5):
        maca_preco = 1.5
    if(kilos > 8):
        porcent = 0.9
    return ((morango_preco * morango_kg) + (maca_preco * maca_kg)) * porcent


morango_kg = int(input("Quilos de morango: "))
maca_kg = int(input("Quilos de morango: "))
total = valor_pago(morango_kg, maca_kg)
print(total)
