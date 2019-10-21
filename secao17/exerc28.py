
class Microondas:
    def __init__(self):
        self.__ligado = 1

    def ligar(self):
        self.__ligado = 1

    def desligar(self):
        self.__ligado = 0


    def imprimir(self):
        if self.__ligado == 1:
            print(f'=== DADOS DO MICROONDAS ===\n')
        else:
            print('O Microondas esta desligado!!')

micro1 = Microondas()
micro1.desligar()
micro1.ligar()
micro1.imprimir()