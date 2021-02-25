'''Faça um programa para o cálculo de uma folha de pagamento,
sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e
3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde
ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a
quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
Salário Bruto: (5 * 220)        : R$ 1100,00
    (-) IR (5%)                     : R$   55,00
    (-) INSS ( 10%)                 : R$  110,00
    FGTS (11%)                      : R$  121,00
    Total de descontos              : R$  165,00
    Salário Liquido                 : R$  935,00
'''
valor_hora = float(input("Valor da hora: "))
quantidade_hora = int(input("Horas trabalhadas: "))
salario_bruto = valor_hora * quantidade_hora
inss = 0.1
fgts = 0.11
porcentagem = 0.03 + fgts + inss
ir = 0.0
if(salario_bruto > 900):
    ir += 0.05
if(salario_bruto > 1500):
    ir += 0.05  # 10% total IR
if(salario_bruto > 2500):
    ir += 0.1   # 20% total IR
porcentagem = porcentagem + ir
reais_ir = salario_bruto * ir
reais_inss = inss * salario_bruto
reais_fgts = fgts * salario_bruto
descontos = salario_bruto * porcentagem
salario_liquido = salario_bruto - descontos
print("Salário Bruto: ({0} * {1})  : R$ {2},00".format(
    valor_hora, quantidade_hora, salario_bruto))
print("(-) IR ({0}%)          : R$ {1},00".format(ir*100, reais_ir))
print("(-) INSS ({0}%)         : R$ {1},00".format(int(inss*100), reais_inss))
print("FGTS ({0}%)             : R$ {1},00".format(int(fgts*100), reais_fgts))
print("Total de descontos     : R$ {0},00".format(int(descontos)))
print("Salário Liquido        : R$ {0},00".format(int(salario_liquido)))
