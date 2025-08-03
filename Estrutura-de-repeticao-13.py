'''
Faça um programa que peça dois números, base e expoente, calcule e mostre
o primeiro número elevado ao segundo número.Não utilize a função de potência da linguagem.
'''
import math
def valida_entrada(mensagem):
    '''
    Função que valida a entrada dada pelo usuário.
    :param: mensagem: mensagem dada ao usuário.
    :return: entrada: retorna o valor da entrada.
    '''
    while True:
        try:
            entrada = int(input(mensagem))
            return entrada
        except ValueError as ve:
            print(f"Entrada inválida, por favor digite um número.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
def calcula_exponencial(base, expoente):
    '''
    Função que retorna o cálculo de base e expoente sem usar a função de potência.
    :param base: base da potência
    :param expoente: expoente da potência
    :return: resultado: retorna o valor do cálculo.
    '''
    resultado = 1
    for i in range(expoente):
        resultado *= base

    return resultado

base = valida_entrada("Digite a base: ")
expoente = valida_entrada("Digite o expoente: ")
resultado = calcula_exponencial(base, expoente)
print(f"{base}^{expoente} = {resultado:.2f}")