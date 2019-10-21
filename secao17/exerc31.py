
class Microondas:
    def __init__(self):
        self.__ligado = 0
        self.__porta_aberta = 0

    def ligar(self):
        if self.__porta_aberta == 0:
            self.__ligado = 1
        else:

            print('Feche a porta do microondas antes de liga-lo!!')

    def desligar(self):
        self.__ligado = 0

    def fecharPorta(self):
        self.__porta_aberta = 0

    def abrirPorta(self):
        self.__porta_aberta = 1
        self.desligar()



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


micro1.ligar()
micro1.abrirPorta()

micro1.imprimir()