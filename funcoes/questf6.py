'''Faça um programa que converta da notação de 24 horas para a notação de 12
horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é
dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a
conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’
para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um
parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita
que o usuário repita esse cálculo para novos valores de entrada todas as vezes
que desejar.'''


def converte_horas(horas):
    horas_convertidas = horas % 12
    if horas % 12 == 0:
        horas_convertidas = 12
    return horas_convertidas


def horario_12(horas, minutos):
    turno = "Horario Invalida"
    if 12 > horas < 24:
        turno = "P.M"
    elif 0 > horas <= 12:
        turno = "A.M"
    else:
        return turno
    novas_horas = converte_horas(horas)
    horario_convertido = "{0}:{1} {2}".format(novas_horas, minutos, turno)
    return horario_convertido


print("Para sair do programa: -1")
horario = 0
while horario != "-1":
    horario = input("Horario: ")
    if(horario == "-1"):
        break
    hora_minuto = horario.split(":")
    horas, minutos = hora_minuto[0], hora_minuto[1]
    horario_convertido = horario_12(horas, minutos)
    print(horario_convertido)
