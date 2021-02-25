'''Faça um Programa que peça uma data no formato dd/mm/aaaa e determine
se a mesma é uma data válida '''


def valida_data(day, mouth, year):
    valid = "Data Invalida"
    if(0 < day <= 31):
        if(0 < mouth <= 12):
            if(year > 0):
                valid = "Data Valida"
    return valid


data = input("Data: ")
date = data.split("/")
day = int(date[0])
mouth = int(date[1])
year = int(date[2])
print("valida_data(day, mouth, year)")
