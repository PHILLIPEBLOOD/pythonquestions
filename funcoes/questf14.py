'''Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas,
com um número em cada posição e no qual a soma das linhas, colunas e diagonais
é a mesma.Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
8  3  4
1  5  9
6  7  2
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos
com as características acima. Dica: produza todas as combinações possíveis e
verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece
ser mais simples que usar uma matriz 3x3. '''
import random


def verifica_satanas(vetor):
    coluna = linha = diagonal = 0
    i = 0
    for n in range(0, 9):
        if i != int(n/3):
            if linha != 15 != coluna and diagonal != 15:
                return False
            i = int(n/3)
            coluna = linha = diagonal = 0
        linha += vetor[n]
        if n % 3 == i:
            coluna += vetor[n]
        if n % 4 == i:
            diagonal += vetor[n]
    return True


satanas = []
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 0
while n < 10:
    numero = random.randint(1, 10)
    satanas.append(numero)
    if n % 10 == 9 and verifica_satanas(satanas):
        i = 0
        print(n)
        while i <= n:
            if i % 3 == 2:
                print(satanas[i])
            else:
                print(satanas[i], end=", ")
            i += 1
        satanas = []
    n += 1
