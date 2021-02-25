'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a
senha igual ao nome do usuário, mostrando
uma mensagem de erro e voltando a pedir as informações. '''
nome_de_usuario = input("Usuário: ")
print("Digite rápido e aperte enter, talvez ninguém veja! ")
senha = input("Senha: ")
while(nome_de_usuario == senha):
    print("\tERROR")
    nome_de_usuario = input("Usuário: ")
    senha = input("Senha: ")
