'''Faça um Programa que verifique se
uma letra digitada é vogal ou consoante. '''
char = input("Digite uma letra: ")
digitada = "Consoante"
vogais = ['a', 'e', 'i', 'o', 'u']
if char in vogais:
    digitada = "Vogal"
print(digitada)
