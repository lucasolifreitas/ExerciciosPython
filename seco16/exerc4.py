"""
Crie uma classe Televisão e uma classe ControleRemoto que pode controlar o volume
e trocar os canais da televisão

- O controle de volume permite aumentar ou diminuir a potência do volume de som em uma unidade de cada vez;
- O controle de canal também permite aumentar e diminuir o número do canal em uma unidade,
porém, também possibilita trocar um canal indicado;
- Também devem existir métodos para consultar o valor do volume de som e o canal selecionado.
"""


class Televisao:

    def __init__(self, volume_max, qtd_canais, ligada=True, canal_atual=3, volume_atual=5):
        self.__volume_max = volume_max
        self.__qtd_canais = qtd_canais
        self.__ligada = ligada
        self.__canal_atual = 3
        self.__volume_atual = (volume_max * 0.1)

    def desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            print('A TV está desligada!')

    def ligar(self):
        if not self.__ligada:
            self.__ligada = True
        else:
            print('A TV está ligada!')

    @property
    def volume_max(self):
        return self.__volume_max

    @property
    def volume_atual(self):
        return self.__volume_atual

    @property
    def qtd_canais(self):
        return self.__qtd_canais

    @property
    def canal_atual(self):
        return self.__canal_atual

    @property
    def ligada(self):
        return self.__ligada

    @volume_atual.setter
    def volume_atual(self, valor):
        self.__volume_atual = valor
        return self.__volume_atual

    @canal_atual.setter
    def canal_atual(self, valor):
        self.__canal_atual = valor
        return self.__canal_atual

    def status(self):
        if self.__ligada:
            print(f'Volume atual: {self.__volume_atual}\n'
                  f'Canal atual: {self.__canal_atual}')
        else:
            print('A TV está desligada!!')


class ControleRemoto:

    def __init__(self, televisao):
        self.__televisao = televisao


    def ligar(self):
        return self.__televisao.ligar()

    def desligar(self):
        return self.__televisao.desligar()

    def volume(self, acao):
        if self.__televisao.ligada:
            if acao == 1:
                if (self.__televisao.volume_atual >= 0) and (
                        self.__televisao.volume_atual < self.__televisao.volume_max):
                    self.__televisao.volume_atual = self.__televisao.volume_atual + 1
                else:
                    print('Volume no máximo!!')
            if acao == 0:
                if (self.__televisao.volume_atual > 0) and (
                        self.__televisao.volume_atual <= self.__televisao.volume_max):
                    self.__televisao.volume_atual = self.__televisao.volume_atual - 1
                else:
                    print('Volume no mínimo!!')
            if acao != 0 and acao != 1:
                print('A ação deve ser:\n'
                      '1 -  para aumentar o volume\n'
                      '0 -  para diminuir o volume')
        else:
            print('A TV esta desligada!!')

    def canal(self, acao):
        if self.__televisao.ligada:
            if acao == 1:
                if (self.__televisao.canal_atual >= 1) and (self.__televisao.canal_atual < self.__televisao.qtd_canais):
                    self.__televisao.canal_atual = self.__televisao.canal_atual + 1
                else:
                    print('Ultimo canal!!')
            if acao == 0:
                if (self.__televisao.canal_atual > 1) and (self.__televisao.canal_atual <= self.__televisao.qtd_canais):
                    self.__televisao.canal_atual = self.__televisao.canal_atual - 1
                else:
                    print('Primeiro canal!!')
            if acao != 0 and acao != 1:
                print('A ação deve ser:\n'
                      '1 -  para ir para o proximo canal\n'
                      '0 -  para ir para o canal anterior')
        else:
            print('A TV esta desligada!')

    def ir_para(self, valor):
        if self.__televisao.ligada:
            if (valor >= 1) and (valor <= self.__televisao.qtd_canais):
                self.__televisao.canal_atual = valor
            else:
                print(f'Escolha um canal entre 1 e {self.__televisao.qtd_canais}!!')
        else:
            print('A TV esta desligada!')


tv1 = Televisao(100, 50)
controle = ControleRemoto(tv1)
controle.volume(1)
controle.canal(1)
controle.ir_para(1)

controle.desligar()
controle.ligar()
controle.ir_para(6)
controle.desligar()
tv1.status()
