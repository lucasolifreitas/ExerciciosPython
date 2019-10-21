
class Microondas:
    def __init__(self):
        self.__ligado = 1
        self.__porta_aberta = 0

    def ligar(self):
        self.__ligado = 1

    def desligar(self):
        self.__ligado = 0


    def imprimir(self):

        if self.__porta_aberta == 1:
            porta = 'Aberta'
        else:
            porta = 'Fechada'

        if self.__ligado == 1:
            print(f'=== DADOS DO MICROONDAS ===\n'
                  f'Porta: {porta}')
        else:
            print('O Microondas esta desligado!!')

micro1 = Microondas()
micro1.desligar()
micro1.ligar()
micro1.imprimir()