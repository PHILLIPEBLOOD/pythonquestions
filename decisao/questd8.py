'''Faça um programa que pergunte o preço de três produtos e
informe qual produto você deve comprar, sabendo que a decisão
é sempre pelo mais barato.'''
produto1 = int(input(""))
produto2 = int(input(""))
produto3 = int(input(""))
mais_barato = produto1
if(produto2 < produto1):
    mais_barato = produto2
if(produto3 < mais_barato):
    mais_barato = produto3
print(mais_barato)
