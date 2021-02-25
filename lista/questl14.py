'''Utilizando listas faça um programa que faça 5 perguntas para uma pessoa
sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da
pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente". '''
cont = []
perguntas = [
    "Telefonou para a vítima?", "Esteve no local do crime?",
    "Mora perto da vítima?", "Devia para a vítima?",
    "Já trabalhou com a vítima?"]
for pergunta in perguntas:
    resposta = int(input(pergunta))
    cont.append(resposta)
total = sum(cont)
julgado = "Inocente"
if(total == 2):
    julgado = "Suspeita"
elif(total == 3 or total == 4):
    julgado = "Cumplice"
elif(total == 5):
    julgado = "Assassino"
print(julgado)
