'''
Faça um programa que use a função valorPagamento para determinar o valor a ser
pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o
valor da prestação e o número de dias em atraso e passar estes valores para a
função valorPagamento, que calculará o valor a ser pago e devolverá este valor
ao programa que a chamou. O programa deverá então exibir o valor a ser pago na
tela. Após a execução o programa deverá voltar a pedir outro valor de prestação
e assim continuar até que seja informado um valor igual a zero para a
prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório
do dia, que conterá a quantidade e o valor total de prestações pagas no dia.
O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem
atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa,
mais 0,1% de juros por dia de atraso. '''


def valorPagamento(valor_prestacao, dias_atraso):
    valor_pago = (0.03 * valor_prestacao) + (0.001 * dias_atraso)
    if dias_atraso == 0:
        valor_pago = valor_prestacao
    return valor_pago


prestacoes = []
valor_prestacao = float(input("Valor prestação: "))
dias_atraso = int(input("Dias atrasados: "))
while valor_prestacao != 0:
    valor_pago = valorPagamento(valor_prestacao, dias_atraso)
    prestacoes.append(valor_pago)
    print("Valor a ser pago: ", valor_pago)
    valor_prestacao = float(input("Valor prestação: "))
    dias_atraso = int(input("Dias atrasados: "))
quantidade = len(prestacoes)
valor_total = sum(prestacoes)
print(quantidade, valor_total)
