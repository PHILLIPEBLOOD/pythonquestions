'''Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de
palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador
poderá errar 6 vezes antes de ser enforcado.
Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!
Digite uma letra: O
A palavra é: _ _ _ _ O
Digite uma letra: E
A palavra é: _ E _ _ O
Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo! '''


def adiciona():
    arq = open('arquivo', 'w')
    n = 0
    while n < 10:
        nome = input("Nome: ")
        nome += "\n"
        arq.write(nome)
        n += 1
    return arq


def forca(nueva, string):
    while nueva != string:
        i = 0
        print(nueva)
        letra = input("Digite uma letra: ")
        while i < len(string):
            if letra == string[i]:
                a = i + 1
                nueva = nueva[:i] + letra + nueva[a:]
            i += 1


nueva = ""
arq_read = open('arquivo', 'r')
for string in arq_read.readlines():
    i = 0
    print(len(string))
    while i < len(string) - 1:
        if(string[i] == " "):
            nueva += " "
        else:
            nueva += "_"
        i += 1
    forca(nueva, string)
arq_read.close()
