class Pessoa:
    def __init__(self, nome, altura, idade):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def dados_pessoa(self):
        print(f'{self.__nome} tem {self.__idade} anos e {self.__altura} de altura')


pessoa1 = Pessoa('Lucas', 1.70, 27)
pessoa1.dados_pessoa()