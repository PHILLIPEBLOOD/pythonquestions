'''O Hipermercado Tabajara está com uma promoção de carnes que é imperdível.
Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos
tipos de carne da promoção, porém não há limites para a quantidade de carne por
cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e
a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as
informações da compra: tipo e quantidade de carne, preço total, tipo de
pagamento, valor do desconto e valor a pagar.
'''
from def_questd28 import descontado, acima_5, valor_carnes

carnes = {0: "File Duplo", 1: "Alcatra", 2: "Picanha"}
pagamentos = ["Sem Tabajara", "Com Tabajara"]
print("Opções: ")
print("\t", carnes)
tipo_carne = input("Opção de carne: ")
quantidade_carne = int(input("Quantidade de carne: "))
tipo_pagamento = int(input("Opção de pagamento: "))
desconto = descontado(tipo_pagamento)
peso_extra = acima_5(quantidade_carne)
preco_carne = valor_carnes(tipo_carne)
valor_parcial = preco_carne * quantidade_carne
valor_total = (valor_parcial + peso_extra) * desconto
print("Tipo de carne:", carnes)
print("Quantidade de carne:", quantidade_carne)
print("Valor parcial:", valor_parcial)
print("Tipo de pagamento:", pagamentos[tipo_pagamento])
print("Desconto:", desconto)
print("Valor total: ", valor_total)
