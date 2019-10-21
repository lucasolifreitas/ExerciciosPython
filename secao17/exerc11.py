
class Moto:
    def __init__(self, marca, modelo, cor, marcha):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__marcha = marcha

    def marchaAcima(self):
        self.__marcha = self.__marcha + 1
        return self.__marcha

    def marchaAbaixo(self):
        self.__marcha = self.__marcha - 1
        return self.__marcha

    def imprimir(self):

        if self.__marcha == 0:
            self.__marcha = 'Neutra'
        elif self.__marcha == 1:
            self.__marcha = 'Primeira'
        elif self.__marcha == 2:
            self.__marcha = 'Segunda'
        else:
            self.__marcha = 'Marcha inválida'


        print(f'=== DADOS DA MOTO ===\n'
              f'Marca: {self.__marca}\n'
              f'Modelo: {self.__modelo}\n'
              f'Cor: {self.__cor}\n'
              f'Marcha: {self.__marcha}')


moto1 = Moto('Marca1', 'CG150', 'Azul', 2)
moto1.marchaAcima()
moto1.imprimir()