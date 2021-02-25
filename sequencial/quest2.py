#Faça um Programa que peça um número e então mostre a mensagem 
# O número informado foi [número].
numero = int(input("Numero: "))
texto = "O número informado foi [{0}]".format(numero)
print(texto)