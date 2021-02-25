'''João Papo-de-Pescador, homem de bem, 
comprou um microcomputador para controlar o rendimento diário de seu trabalho.
 Toda vez que ele traz um peso de peixes maior que o estabelecido pelo
 regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa
 de R$ 4,00 por quilo excedente. João precisa que você faça um programa
 que leia a variável peso (peso de peixes) e calcule o excesso.
 Gravar na variável excesso a quantidade de quilos além do limite e na
 variável multa o valor da multa que João deverá pagar.
 Imprima os dados do programa com as mensagens adequadas.'''
peso = float(input("Peso de peixes: "))
pesoexcedente = 0
if (peso > 50):
    pesoexcedente = peso - 50
multa = pesoexcedente * 4
print("Peso excedente foi de", pesoexcedente)
print("Multa por excesso foi de", multa, "R$")

     