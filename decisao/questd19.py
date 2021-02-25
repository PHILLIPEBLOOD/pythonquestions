'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a
quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros.
Exemplo: 326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101,
311, 111, 25, 20, 10, 21, 11, 1, 7 e 16Faça um Programa que leia um número
inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e
unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros.
Exemplo: 326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101,
311, 111, 25, 20, 10, 21, 11, 1, 7 e 16'''
number = int(input())
casas_decimais = "Numero Invalido"
if(number < 1000):
    unidades = number % 10
    dezenas = ((number % 100) - unidades)/10
    centenas = ((number % 1000) - (unidades + dezenas)) / 100
    casas_decimais = "{0} centenas, {1} dezenas e {2} unidades".format(
        centenas, dezenas, unidades)
print(casas_decimais)
