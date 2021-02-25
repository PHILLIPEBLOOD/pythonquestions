'''Classe Bola: Crie uma classe que modele uma bola:
Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
'''


class Bola:
    cor = ""
    circunferencia = 0.0
    material = ""

    def troca_cor(self, cor):
        self.cor = cor

    def mostra_cor(self):
        print(self.cor)
