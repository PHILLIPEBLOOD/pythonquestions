'''Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
aproximado de download do arquivo usando este link (em minutos). '''
tamanho = float(input("Tamanho do arquivo: "))
velocidade = float(input("Velocidade da rede: "))
segundos = int(tamanho / velocidade)
minutos = segundos / 60
print("{minutos:.2f} minuto(s)".format(minutos=minutos))
