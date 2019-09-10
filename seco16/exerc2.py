class Agenda:
    contador = 0
    minha_agenda = dict()
    def __init__(self, nome, idade, altura):
        self.__numero = Agenda.contador + 1
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
        Agenda.contador = self.__numero
        self.__minha_agenda = Agenda.minha_agenda

    def agenda(self):
        print('criou a agenda!')

    def armazenarPessoa(self):
        pessoa = []
        if Agenda.contador < 10:
            pessoa.append(self.__idade)
            pessoa.append(self.__altura)

            self.__minha_agenda[self.__nome.lower().capitalize()] = pessoa


        else:
            print('Sua Agenda está cheia!')

    def removePessoa(self, nome):
        self.__minha_agenda.pop(nome, 'Contato não encontrado')

    def buscaPessoa(self, nome):
        posicao = 1
        i = 0
        while list(self.__minha_agenda.keys())[i] != nome:
            posicao = posicao + 1
            i = i+1
        print(f'O contato {nome} esta na posição {posicao}')

    def imprimePessoa(self, i):
        nome = list(self.__minha_agenda.keys())[i - 1]
        idade = self.__minha_agenda[list(self.__minha_agenda.keys())[i-1]][0]
        altura = self.__minha_agenda[list(self.__minha_agenda.keys())[i - 1]][1]

        print(f'Na posição {i} se encontra {nome}!')
        print(f'Cujos os dados são:')
        print(f'Idade: {idade} anos')
        print(f'Altura: {altura} metros')

    def imprimeAgenda(self):
        print(self.__minha_agenda)


"""
minha_agenda.ArmazenarPessoa("Joao", 52, 1.81f );
minha_agenda.ArmazenarPessoa("Lara", 49, 1.72f );
minha_agenda.ArmazenarPessoa("Nani", 27, 1.76f );
minha_agenda.ArmazenarPessoa("Rayssa", 26, 1.45f );
minha_agenda.ArmazenarPessoa("Tais", 26, 1.72f );
minha_agenda.ArmazenarPessoa("Enrico", 24, 1.76f );
minha_agenda.ArmazenarPessoa("Gabriel", 23, 1.76f );
minha_agenda.ArmazenarPessoa("Caio", 25, 1.77f );
minha_agenda.ArmazenarPessoa("Jane", 35, 1.65f );
minha_agenda.ArmazenarPessoa("Mauro", 49, 1.81f );
"""
minha_agenda = Agenda("Joao", 52, 1.81)
minha_agenda.armazenarPessoa()
minha_agenda = Agenda('Lucas', 27, 170)
minha_agenda.armazenarPessoa()
minha_agenda = Agenda('ana', 17, 14)
minha_agenda.armazenarPessoa()
minha_agenda = Agenda('maria', 45, 179)
minha_agenda.armazenarPessoa()
minha_agenda = Agenda("Joao", 52, 1.81)
minha_agenda.armazenarPessoa()
minha_agenda = Agenda('Lucas', 27, 170)
minha_agenda.armazenarPessoa()

minha_agenda.removePessoa('Lucas')
minha_agenda.buscaPessoa('Maria')
minha_agenda.imprimePessoa(3)
#minha_agenda.removePessoa('Lucas')
minha_agenda = Agenda('Lucas', 27, 170)
minha_agenda.armazenarPessoa()
minha_agenda.imprimeAgenda()