"""
Escreva um código que apresente a classe Televisor, com atributos, ligado,
canal e volume e, o método imprimir. O método imprimir deve mostrar na tela
os valores de todos os atributos. O atributo ligado será boleano e deverá
indicar o estado atual do televisor, se ligado ou desligado. O atributo canal
deverá indicar o canal em que o televisor está sintonizado. O atributo
volume deverá indicar o volume atual do televisor
"""

class Televisor:

    def __init__(self, canal, volume):
        self.__ligado = 1
        self.__canal = canal
        self.__volume = volume

    def imprimir(self):
        if self.__ligado == 1:
            print(f'=== DADOS DA TV ===\n'
                  f'Canal: {self.__canal}\n'
                  f'Volume: {self.__volume}\n')
        else:
            print('A TV está desligada!')

tv1 = Televisor(3, 10)
tv1.imprimir()
