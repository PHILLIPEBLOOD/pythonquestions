'''
Faça um programa que leia um número indeterminado de valores, correspondentes
a notas, encerrando a entrada de dados quando for informado um valor igual a -1
(que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados,
um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem; '''
numeros = []
numeros_inverso = []
numero = int(input("Numero: "))
while numero != -1:
    numeros.append(numero)
    numero = int(input("Numero: "))
reverse = len(numeros)
cont_abaixo7 = 0
acima_media = 0
soma = sum(numeros)
media = soma / reverse
while reverse >= 0:
    if numeros[reverse] < 7:
        cont_abaixo7 += 1
    if numeros[reverse] > media:
        acima_media += 1
    numeros_inverso.append(numeros[reverse])
    reverse -= 1
for valor in numeros:
    print(valor, end=", ")
for valor in numeros_inverso:
    print(valor, end=", ")
print("Soma:", soma)
print("Media:", media)
print("Quantidade acima da media:", acima_media)
print("Quantidade abaixo de sete:", cont_abaixo7)
