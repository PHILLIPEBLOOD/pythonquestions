'''Data com mês por extenso. Construa uma função que receba uma data no formato
DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA.
Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
'''


def data_extenso(data):
    meses = {
        1: "janeiro",
        2: "fevereiro",
        3: "março",
        4: "abril",
        5: "maio",
        6: "julho",
        7: "junho",
        8: "agosto",
        9: "setembro",
        10: "outubro",
        11: "novembro",
        12: "dezembro"
    }
    data_lista = data.split("/")
    mes = data_lista[1]
    tamanho_dia = len(data_lista[0])
    tamanho_mes = len(data_lista[1])
    tamanho_ano = len(data_lista[2])
    data = data.replace("/", " de ")
    data = data.replace(mes, meses[int(mes)])
    if tamanho_dia != 2:
        data = None
    if tamanho_mes != 2:
        data = None
    if tamanho_ano != 4:
        data = None
    return data


date = input("Digite a data: ")
data = data_extenso(date)
print(data)
