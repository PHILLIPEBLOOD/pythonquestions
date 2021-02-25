'''Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário
(incluindo espaços em branco), conte:
quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.
'''
frase = input()
elementos = ["a", "b", "c", "d", "e"]
cont_vogais = cont_esp = 0
for char in frase:
    if char == " ":
        cont_esp += 1
        break
    for elemento in elementos:
        if elemento == char:
            cont_vogais += 1
print(cont_esp, "espaços em branco")
print(cont_vogais, "vogais na frase")
