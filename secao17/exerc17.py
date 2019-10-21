"""
Escreva um código que apresente a classe Eletodoméstico, com atributo çigado e o método
imprimir. O método imprimir deve mostrar na tela os valores de todos os atributos. O atributo
ligado será boleano e deverá indicar o estado atual do eletrodomestico, se ligado ou desligado
"""

class Eletrodomestico:

    def __init__(self):
        self.__ligado = 1

    def imprimir(self):
        if self.__ligado == 1:
            print('O aparelho esta ligado')
        else:
            print('O aparelho está desligado')


eletro = Eletrodomestico()
eletro.imprimir()