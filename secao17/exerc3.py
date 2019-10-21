"""
Escreva um código que apresente a classe Quadrado, com atributos lado, área e perímetro e,
os métodos calcularArea, calcularPerimetro e imprimir. Os métodos calcularArea e calcularPerimetro
devem efetuar seus respectivos cálculos e colocar os valores nos atributos area e perimetro.
O método imprimir deve mostrar na tela os valores de todos os atributos.
Salienta-se que a área de um quadrado é obtida pela fórmula (lado * lado) e o perímetro por (4 * lado)
"""

class Quadrado:
    def __init__(self, lado):
        self.__lado = lado
        self.__area = self.calcularArea()
        self.__perimetro = self.calcularPerimetro()

    def calcularArea(self):
        area = (self.__lado * self.__lado)
        return area

    def calcularPerimetro(self):
        perimetro = (4 * self.__lado)
        return perimetro

    def imprimir(self):
        print(f'O quadrado tem lado: {self.__lado}\n'
              f'Sua área é: {self.__area} m²\n'
              f'Seu perímetro é: {self.__perimetro} m')


quad1 = Quadrado(3)
quad1.imprimir()

