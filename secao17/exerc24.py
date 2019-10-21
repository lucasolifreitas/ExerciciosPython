
class Televisor:

    def __init__(self, canal, volume, numero_canais, volume_maximo):
        self.__ligado = 1
        self.__canal = canal
        self.__volume = volume
        self.__numero_canais = numero_canais
        self.__volume_maximo = volume_maximo

    def ligar(self):
        self.__ligado = 1

    def desligar(self):
        self.__ligado = 0


    def canalAcima(self):
        if self.__canal == self.__numero_canais:
            self.__canal = 1
        else:
            self.__canal = self.__canal + 1

    def canalAbaixo(self):
        if self.__canal == 1:
            self.__canal = self.__numero_canais
        else:
            self.__canal = self.__canal - 1

    def imprimir(self):
        if self.__ligado == 1:
            print(f'=== DADOS DA TV ===\n'
                  f'Canal: {self.__canal}\n'
                  f'Volume: {self.__volume}\n')
        else:
            print('A TV está desligada!')

tv1 = Televisor(3, 10, 50, 100)
tv1.desligar()
tv1.ligar()
tv1.imprimir()
