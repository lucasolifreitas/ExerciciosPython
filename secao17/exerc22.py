"""
Adição dos métodos ligar() e desligar()
"""

class Televisor:

    def __init__(self, canal, volume):
        self.__ligado = 1
        self.__canal = canal
        self.__volume = volume

    def ligar(self):
        self.__ligado = 1

    def desligar(self):
        self.__ligado = 0

    def imprimir(self):
        if self.__ligado == 1:
            print(f'=== DADOS DA TV ===\n'
                  f'Canal: {self.__canal}\n'
                  f'Volume: {self.__volume}\n')
        else:
            print('A TV está desligada!')

tv1 = Televisor(3, 10)
tv1.desligar()
tv1.ligar()
tv1.imprimir()
