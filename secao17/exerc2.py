"""
Baseando-se no exerc1 adicione um método construtor que permita a definição de todos
os atributos no momento da instanciação do objeto
"""
#resposta igual ao exerc1

class Pessoa:
    def __init__(self, nome, endereco, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    def imprimir(self):
        print(f'Nome: {self.__nome}\n'
              f'Endereço: {self.__endereco}\n'
              f'Telefone: {self.__telefone}')


pessoa1 = Pessoa('Lucas', 'Rua Projetada', '9999-9999')
pessoa1.imprimir()
