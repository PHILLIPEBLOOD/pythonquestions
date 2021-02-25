'''Jogo de Craps. Faça um programa de implemente um jogo de Craps.
O jogador lança um par de dados, obtendo um valor entre 2 e 12.
Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você
perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu
"Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número
novamente. Você perde, no entanto, se tirar um 7 antes de tirar este
Ponto novamente. '''
import random


def tent(par_dados):
    novo_par = random.randint(2, 12)
    print(novo_par)
    var = "Venceu"
    if novo_par == 7:
        var = "Craps"
    elif par_dados != novo_par:
        var = tent(par_dados)
    return var


def craps(par_dados):
    print(par_dados)
    var = "Craps"
    if par_dados == 11 or par_dados == 7:
        var = "Venceu"
    elif 4 <= par_dados <= 10:
        var = tent(par_dados)
    return var


par_dados = random.randint(2, 12)
print(craps(par_dados))
