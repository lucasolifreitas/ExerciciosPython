"""
Crie uma classe denominada Elevador para armezenar as informações de um elevador
dentro de um prédio. A classe deve armazenar o andar atual (térro = 0), total de andares no prédio,
excluindo o térreo, capacidade do elevador, e quantas pessoas estão presentes nele.

A classe deve também disponibilizar os seguintes métodos:

- Inicializa: que deve receber como parâmetros a capacidade do elevador e o total de andares no prédio
(os elevadores sempre começam no térreio e vazio);
- Entra: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver espaço)
- Sai: para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele)
- Sobe: para subir um andar (não deve subir se já estiver no último andar)
- Desce: para descer um andar (não deve descer se já estiver no térreo)
- Encapsular todos os atributos da classe ( criar os métodos set e get)

"""

class Elevador:

    def __init__(self, andar_atual, tot_andares, capacidade_elevador, pessoas_elevador):
        self.__andar_atual = andar_atual
        self.__tot_andares = tot_andares
        self.__capacidade_elevador = capacidade_elevador
        self.__pessoas_elevador = pessoas_elevador

    @property
    def andar_atual(self):
        return self.__andar_atual

    @property
    def tot_andares(self):
        return self.__tot_andares

    @property
    def capacidade_elevador(self):
        return self.__capacidade_elevador

    @property
    def pessoas_elevador(self):
        return self.__pessoas_elevador

#  def __init__(self, andar_atual, tot_andares, capacidade_elevador, pessoas_elevador):
    def estado_elevador(self):
        print(f'Andar atual: {self.__andar_atual}\n'
              f'Total de Andares: {self.__tot_andares}\n'
              f'Capacidade do Elevador: {self.__capacidade_elevador}\n'
              f'Pessoas no elevador: {self.__pessoas_elevador}')

    def inicializa(self):
        return Elevador(0, self.__tot_andares, self.__capacidade_elevador, 0)

    def entra(self, pessoas):
        if (self.__capacidade_elevador - self.__pessoas_elevador) >= pessoas:
            self.__pessoas_elevador = self.__pessoas_elevador + pessoas
        else:
            print('Não tem espaço neste elevador!!')

    def sai(self, pessoa):
        if self.__pessoas_elevador > 0:
            self.__pessoas_elevador = self.__pessoas_elevador - pessoa

    def sobe(self):
        if (self.__andar_atual + 1) <= (self.__tot_andares):
            self.__andar_atual = self.__andar_atual + 1
        else:
            print('Você já está no ultimo andar!!')

    def desce(self):
        if (self.__andar_atual != 0):
            self.__andar_atual = self.__andar_atual -1
        else:
            print('Voce está no térreo!!')
# def __init__(self, andar_atual, tot_andares, capacidade_elevador, pessoas_elevador):




teste = Elevador(0, 3, 10, 0)
teste.inicializa()
teste.entra(5)
teste.entra(4)
teste.entra(1)
teste.desce()
teste.estado_elevador()