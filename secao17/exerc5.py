"""
Escreva um código que apresente a classe Retângulo, com atributos
comprimento, largura, área e perímetro e, os métodos calcularArea,
calcularPerimetro e imprimir. Os métodos calcularArea e calcularPerimetro
devem efetuar seus respectios cálculos e colocar os valores nos atributos
area e permetro. Salienta-se que a área de um retangulo é obtida pela formula
(comprimento * largura) e o perímetro por (2 * comprimento) + (2*largura)
"""

class Retangulo:
    def __init__(self, comprimento, largura):
        self.__comprimento = comprimento
        self.__largura = largura
        self.__area = self.calcularArea()
        self.__perimetro = self.calcularPerimetro()

    def calcularArea(self):
        area = (self.__comprimento * self.__largura)
        return area

    def calcularPerimetro(self):
        perimetro = ((2*self.__comprimento)  + (2*self.__largura))
        return perimetro

    def imprimir(self):
        print(f'==== DADOS DO RETÂNGULO === \n'
              f'Comprimento: {self.__comprimento} m\n'
              f'Largura: {self.__largura} m\n'
              f'Área: {self.__area} m²\n'
              f'Perímetro: {self.__perimetro} m')


retangulo1 = Retangulo(2,3)
retangulo1.imprimir()