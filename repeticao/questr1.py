'''Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o
usuário informe um valor válido. '''
nota = int(input("Digite uma nota: "))
while(nota >= 10 or nota < 0):
    print("Valor Invalido! ")
    nota = int(input("Digite uma nota: "))
