''' Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.'''
dia = input("Dia: ")
dias = {
    "1": "Domingo",
    "2": "Segunda",
    "3": "Terça",
    "4": "Quarta",
    "5": "Quinta",
    "6": "Sexta",
    "7": "Sabado"
}
try:
    semana = dia + "-" + dias[dia]
    print(semana)
except KeyError:
    print("Valor Invalido")
