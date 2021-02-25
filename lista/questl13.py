'''Faça um programa que receba a temperatura média de cada mês do ano e
armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e
mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram
(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ). '''
temperaturas = []
meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}
for n in range(1, 13):
    temperatura = float(input("Temperatura: "))
    temperaturas.append(temperatura)
media = sum(temperaturas) / 12
for n in range(1, 13):
    if(temperaturas[n-1] > media):
        print(temperaturas[n-1], meses[n])
