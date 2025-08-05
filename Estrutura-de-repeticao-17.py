'''
Faça um programa que calcule o
fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
'''
def valida_entrada(mensagem):
    '''
    Função que valida entrada do usuário.
    :param mensagem:
    :return: entrada: valor dado pelo usuario após conversão.
    '''
    while True:
        try:
            entrada = int(input(mensagem))
            if entrada >= 0:
                return entrada
            else:
                print(f"Por favor, digitar um numero inteiro maior ou igual a zero. ")
        except ValueError as ve:
            print(f"Entrada inválida, por favor digite um número inteiro: {ve}")
        except Exception as e:
            print(f"Ocorreu um erro ")

def calcula_fatorial(inteiro):
    '''
    Função que calcula fatorial.
    :param inteiro: Inteiro recebido pelo usuário.
    :return: inteiro
    '''
    if inteiro == 0:
        fatorial = 1
        return fatorial
    else:
        fatorial = 1
        for i in range(1, inteiro + 1):
            fatorial *= i
        return fatorial
numero_inteiro = valida_entrada("Digite um número inteiro: ")
resultado_fatorial = calcula_fatorial(numero_inteiro)
print(f"{numero_inteiro}! é {resultado_fatorial}")

    
