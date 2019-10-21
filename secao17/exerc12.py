
class Moto:
    def __init__(self, marca, modelo, cor, marcha, menor_marcha, maior_marcha):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__marcha = marcha
        self.__menor_marcha = menor_marcha
        self.__maior_marcha = maior_marcha

    def marchaAcima(self):
        if self.__marcha < self.__maior_marcha:
            self.__marcha = self.__marcha + 1
            return self.__marcha
        else:
            self.__marcha = f'Marcha inválida! \n' \
                            f'Esse modelo trabalha com marcha entre {self.__menor_marcha} e {self.__maior_marcha}'
            return self.__marcha

    def marchaAbaixo(self):
        if self.__marcha > self.__menor_marcha:
            self.__marcha = self.__marcha - 1
            return self.__marcha
        else:
            self.__marcha = f'Marcha inválida! \n' \
                            f'Esse modelo trabalha com marcha entre {self.__menor_marcha} e {self.__maior_marcha}'
            return self.__marcha

    def imprimir(self):

        print(f'=== DADOS DA MOTO ===\n'
              f'Marca: {self.__marca}\n'
              f'Modelo: {self.__modelo}\n'
              f'Cor: {self.__cor}\n'
              f'Marcha: {self.__marcha}')


moto1 = Moto('Marca1', 'CG150', 'Azul', 2, 0, 5)
moto1.marchaAbaixo()
moto1.marchaAbaixo()
moto1.marchaAbaixo()
moto1.imprimir()