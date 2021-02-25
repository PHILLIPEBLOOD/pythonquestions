'''Leet spek generator. Leet é uma forma de se escrever o alfabeto latino
usando outros símbolos em lugar das letras, como números por exemplo. A própria
palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete
uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo
muito usada para confundir os iniciantes e afirmar-se como parte de um grupo.
Pesquise sobre as principais formas de traduzir as letras. Depois, faça um
programa que peça uma texto e transforme-o para a grafia leet speak. '''
dicionario = {
    "a": "/-\\",
    "b": "|3",
    "c": "(",
    "d": "o|",
    "e": "3",
    "f": "|#",
    "g": "6",
    "h": "|-|",
    "i": "!",
    "j": ";",
    "k": "|<",
    "l": "|_",
    "m": "/\\/\\",
    "n": "n",
    "o":	"?p",
    "p": "|^",
    "q": "q",
    "r": "[z",
    "s": "5",
    "t":	"7",
    "u":	"|_|",
    "v":	"\\/",
    "w":	"vv",
    "x":	"><",
    "y":	"`/",
    "z": 	"2"
}
palavra = input("")
tam = len(palavra)
for n in range(0, tam):
    letra = palavra[n]
    print(dicionario[letra], end="")
print()
