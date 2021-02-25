'''Faça um Programa que verifique se uma letra digitada é "F" ou "M.
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''
sexo = input("Sexo: ")
tipo = "Invalido"
if(sexo == "F"):
    tipo = "Feminino"
elif(sexo == "M"):
    tipo = "Masculino"

print(tipo)
