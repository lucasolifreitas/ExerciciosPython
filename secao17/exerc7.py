"""
Escreva um código que apresente a classe Circulo, com atributos raio, área e perímetro e, os
métodos calcularArea, calcularPerimetro e imprimir. Os métodos calcularArea e calcularPerímetro devem
efetuar seus respectivos cálculos e colocar os valores nos atributos área e perimetro.
O método imorimir deve mostrar na tela os valores de todos os atributos. Salienta-se que a área de um
círculo é obtida pela formula (pi * raio * raio) e o perímetro por (2 * pi * raio), onde pi = 3.141516

"""


class Circulo:
    pi = 3.141516

    def __init__(self, raio):
        self.__raio = raio
        self.__area = self.calcularArea()
        self.__perimetro = self.calcularPerimetro()

    def calcularArea(self):
        area = (self.pi * self.__raio * self.__raio)
        return area

    def calcularPerimetro(self):
        perimetro = (2 * self.pi * self.__raio)
        return perimetro

    def imprimir(self):
        print(f'=== DADOS DO CÍRCULO === \n'
              f'Raio: {self.__raio} m\n'
              f'Área: {self.__area:.4f} m²\n'
              f'Perímetro: {self.__perimetro:.4f} m')


circulo1 = Circulo(4)
circulo1.imprimir()
