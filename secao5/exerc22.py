idade = int(input('Digite sua idade: '))
tempo_servico = int(input('Informe o tempo de serviço: '))

if (idade >= 65) or (tempo_servico > 30) or (idade >= 60 and tempo_servico >= 25):
    print('O funcionario pode ser aposentar!!')
else:
    print('Não pode ser aposentar!')

