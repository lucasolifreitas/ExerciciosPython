"""
Baseando-se no exerc3 adicione um método construtor que permita a definição de todos
os atributos no momento da instanciação do objeto
"""


class Quadrado:
    def __init__(self, lado, area, perimetro):
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

