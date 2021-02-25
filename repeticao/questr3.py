'''Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd'; '''
nome = input("Nome: ")
while len(nome) < 3:
    nome = input("Nome: ")
idade = int(input("Idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Idade: "))
salario = float(input("Salario: "))
while salario < 0:
    salario = float(input("Salario: "))
sexo = input("Sexo: ")
while "f" != sexo != "m":
    sexo = input("Sexo: ")
estado_civil = input("Estado Civil: ")
while ("s" != estado_civil != "c" and "v" != estado_civil != "d"):
    estado_civil = input("Estado Civil: ")
