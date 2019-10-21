"""
Escreva um código que apresente a classe Microondas, com atributo ligado e método imprimir.
O método imprimir deve mostrar na tela os valores de todos os atributos. O atributo ligado será boleano
e deverá indicar o estado atual do microondas, se ligado ou desligado.
"""

class Microondas:
    def __init__(self):
        self.__ligado = 1


    def imprimir(self):
        if self.__ligado == 1:
            print(f'=== DADOS DO MICROONDAS ===\n')
        else:
            print('O Microondas esta desligado!!')

micro1 = Microondas()
micro1.imprimir()