def soma(a, b):
    if type(a) == str or type(b) == str:
        raise TypeError("Só números tipo int ou float são permitidos")

    else:
        soma = a + b
        return soma


def subtracao(a, b):
    subtracao = a - b
    return subtracao


def multiplicacao(a, b):
    if type(a) == str or type(b) == str:
        raise TypeError("Só números tipo int ou float são permitidos")
    else:
        multiplicacao = a * b
        return multiplicacao


def divisao(a, b):
    if b != 0:
        divisao = a / b
        return divisao
    if b == 0:
        raise Exception('Divisão inválida')
