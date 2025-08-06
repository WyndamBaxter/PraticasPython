"""
Faça um programa que, dado um conjunto de N números, determine o
menor valor, o maior valor e a soma dos valores.
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""

def calcula_maior_menor_soma(lista_de_numeros):
    '''
    Função que calcula o maior, menor e a soma dos números dados.
    :param lista_de_numeros: Lista de números enviadas pelo usuário.
    :return: resultado: Lista com valores, nessa ordem, de menor, maior e
                        soma dos valores de lista_de_números.
    '''

    return [min(lista_de_numeros), max(lista_de_numeros), sum(lista_de_numeros)]
    '''
    Opção 1
    resultado = []
    dados_resultado =[
        (0, min, lista_de_numeros),
        (1, max, lista_de_numeros),
        (2, sum, lista_de_numeros)
    ]
    for posicao, funcao, lista in dados_resultado:
        resultado.append(funcao(lista))
    return resultado
    '''
    '''
    Opção 2:
    resultado[0] = min(lista_de_numeros)
    resultado[1] = max(lista_de_numeros)
    resultado[2] = sum(lista_de_numeros)
    '''
#Programa principal
conjunto_n = [1, 5, 6, 48, 8, 23, 34]
lista_resultado = calcula_maior_menor_soma(conjunto_n)
print(f"O menor valor da lista N é: {lista_resultado[0]}, o maior é: {lista_resultado[1]} e a soma é:{lista_resultado[2]}.")


