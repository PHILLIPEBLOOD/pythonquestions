'''Embaralha palavra. Construa uma função que receba uma string como parâmetro
e devolva outra string com os carateres embaralhados. Por exemplo: se função
receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra
combinação possível, de forma aleatória. Padronize em sua função que todos os
caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de
como foram digitados. '''
import random


def embaralhados(nome):
    nome = nome.lower()
    n = 1
    for n in range(0, len(nome)):
        alea = random.randint(0, len(nome))
        alea2 = random.randint(0, len(nome))
        nome[alea], nome[alea2] = nome[alea2], nome[alea]
    return nome
