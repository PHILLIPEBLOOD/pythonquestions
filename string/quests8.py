'''Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é
idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e
OVO são palíndromos. Em textos mais complexos os espaços e pontuação são
ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os
espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres,
mostre−a e diga se é um palíndromo ou não. '''
palindromo = input().upper
remover = " "
tam = len(palindromo) - 1
texto = "Não é palindromo"
if remover in palindromo:
    palindromo.remove(remover)
if palindromo == palindromo[-1:tam]:
    texto = "É um palindromo"
print(texto)
