"""
Escreva um código que apresente a classe Moto, com atributos marca,
modelo, cor e marcha e, o método imprimir. O método imprimir deve mostrar na tela
os valores de todos os atributos. O atributo marcha indica em que a marcha a Moto se
encontra no momento, sendo representado de forma inteira, onde 0 - neutro, 1- primeira,
2 - segunda, etc.

"""

class Moto:
    def __init__(self, marca, modelo, cor, marcha):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__marcha = marcha

        if self.__marcha == 0:
            self.__marcha = 'Neutra'
        elif self.__marcha == 1:
            self.__marcha = 'Primeira'
        elif self.__marcha == 2:
            self.__marcha = 'Segunda'
        else:
            self.__marcha = 'Marcha inválida'




    def imprimir(self):
        print(f'=== DADOS DA MOTO ===\n'
              f'Marca: {self.__marca}\n'
              f'Modelo: {self.__modelo}\n'
              f'Cor: {self.__cor}\n'
              f'Marcha: {self.__marcha}')


moto1 = Moto('Marca1', 'CG150', 'Azul', 2)
moto1.imprimir()