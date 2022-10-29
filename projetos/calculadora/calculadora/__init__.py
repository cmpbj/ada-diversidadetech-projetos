from calculadora.funcoes import soma
from calculadora.funcoes import subtracao
from calculadora.funcoes import divisao
from calculadora.funcoes import multiplicacao


def calcule():

    numero_a = float(input('Digite um número: '))
    numero_b = float(input('Digite um número: '))
    operacao = input(
        "Escolha a operação. Opções válidas: 'soma', 'subtracao', 'divisao', 'multiplicacao', '+', '-', '/', '*': ")

    operacao = operacao.lower()

    if operacao == 'soma' or operacao == '+':
        print(soma(numero_a, numero_b))

    elif operacao == 'multiplicacao' or operacao == '*':
        print(multiplicacao(numero_a, numero_b))

    elif operacao == 'subtracao' or operacao == '-':

        print(subtracao(numero_a, numero_b))

    elif operacao == 'divisao' or operacao == '/':

        print(divisao(numero_a, numero_b))
    else:
        print('Operação inválida ou números inválidos')
