'''Desenha moldura. Construa uma função que desenhe um retângulo usando os
caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e
colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor
máximo é 20. Se valores fora da faixa forem informados, eles devem ser
modificados para valores dentro da faixa de forma elegante. '''


def inicial_lincol(linhas, colunas):
    coluna = ""
    linha = ""
    cont_colunas = 0
    cont_linhas = 0
    while (cont_colunas < linhas) and (cont_colunas < colunas):
        if cont_linhas == 0:
            linha = "+"
            for n in range(colunas):
                coluna += "-"
            linha = "+"
        cont_linhas += 1
        cont_colunas += 1
    return linha + coluna + linha


def linha(linhas, colunas):
    linhas_colunas = ""
    cont_colunas = 0
    cont_linhas = 0
    coluna = ""
    linha = ""
    while cont_colunas < cont_linhas:
        if cont_linhas == 0:
            linha = "|"
            for i in range(linha):
                coluna += " "
        cont_linhas += 1
        cont_colunas += 1
        linhas_colunas = linha + coluna + linha
    return linhas_colunas


def ultima_linha(linhas, colunas):
    linha_final = ""
    cont_linhas = 0
    cont_colunas = 0
    linha = "+"
    coluna = ""
    while (cont_linhas < linhas) and (cont_colunas < colunas):
        if cont_linhas == 0:
            for n in range(colunas):
                coluna += "-"
        cont_linhas += 1
        cont_colunas += 1
    linha_final += linha + coluna + linha
    return linha_final


linhas = int(input("Informe o número de linhas: "))
colunas = int(input("Informe o número de colunas: "))
print(inicial_lincol(linhas, colunas))
print(linha(linhas, colunas))
print(ultima_linha(linhas, colunas))
