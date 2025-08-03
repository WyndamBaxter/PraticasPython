'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de
qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele
deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
'''

def valida_entrada(mensagem):
    '''
    Função que valida a entrada do usuário.
    :param mensagem: mensagem do usuário.
    :return: numero: número recebido pelo usuário.
    '''
    while True:
        try:
            numero = int(input(mensagem))
            if 0 < numero <= 10:
                return numero
            else:
                print("Por favor, digite um número entre 1 e 10")
        except ValueError as ve:
            print(f"Entrada inválida, por favor digite um número: {ve}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

def calcula_operacao(numero):
    operacao = {}
    for number in range(1, 11):
        operacao[number] = number*numero
    return operacao
#programa principal
numero = valida_entrada("Digite um número entre 1 e 10: ")
resultado = calcula_operacao(numero)

print(f"Tabuada do numero {numero}")
for multiplicador, resultado in resultado.items():
    print(f"{numero} X {multiplicador} = {resultado}")
