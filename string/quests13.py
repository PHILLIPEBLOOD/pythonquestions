'''Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que
adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa
terá uma lista de palavras lidas de um arquivo texto e escolherá uma
aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao
final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou
perdeu o jogo. '''
from random import sample

arq = open('arquivo', 'r')
a = 0
lista = []
for string in arq.readlines():
    lista.append(string)
tam = len(lista)
print(lista)
alea = sample(range(0, tam), 1)
aleatorio = alea[0]
palavra = lista[aleatorio]
tam_palavra = len(palavra) - 1
positions = sample(range(0, tam_palavra), tam_palavra)
for n in positions:
    print(palavra[n], end="")
jogo = "Perdeu o jogo"
for n in range(0, tam_palavra):
    text = input("\nTente acertar a palavra: ")
    if palavra[0:tam_palavra] == text:
        jogo = "Ganhou o jogo"
        break
print(jogo)
arq.close()
