'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação
sobre a participação da pessoa no crime. Se a pessoa responder positivamente a
2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como
"Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente". '''
print("0 para Não,\t 1 para sim")
julga = int(input("Esteve no local do crime?"))
julga += int(input("Telefonou para a vítima?: "))
julga += int(input("Mora perto da vítima?: "))
julga += int(input("Devia para a vítima?: "))
julga += int(input("Já trabalhou com a vítima?: "))
julgado = "Inocente"
if(julga == 2):
    julgado = "Suspeita"
elif(julga == 3 or julga == 4):
    julgado = "Cumplice"
elif(julga == 5):
    julgado = "Assassino"
print(julgado)
