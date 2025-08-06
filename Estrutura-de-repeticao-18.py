"""
Faça um programa que, dado um conjunto de N números, determine o
menor valor, o maior valor e a soma dos valores.
"""
def valida_entrada(mensagem):
    '''
    Função que valida a entrada dos números do usuário.
    :param mensagem: mensagem do usuário.
    :return: entrada: retorna
    '''
    while True:
        try:
            entrada = float(input(mensagem))
            return entrada
        except ValueError as ve:
            print(f"Por favor digite um número. {ve}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

def valida_conjunto(pergunta):
    '''
    Função que valida o tamanho do conjunto recebido
    :param pergunta: recebe mensagem do usuário sobre tamanho do conjunto.
    :return: tamanho_conjunto: retorna o tamanho do conjunto.
    '''
    while True:
        try:
            tamanho_conjunto = int(input(pergunta))
            if tamanho_conjunto > 0:
                return tamanho_conjunto
        except ValueError as ve:
            print(f"Por favor digite um número inteiro maior que zero: {ve}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")


def calcula_maior_menor_soma(lista_de_numeros):
    '''
    Função que calcula o maior, menor e a soma dos números dados.
    :param lista_de_numeros: Lista de números enviadas pelo usuário.
    :return: resultado: Lista com valores, nessa ordem, de menor, maior e
                        soma dos valores de lista_de_números.
    '''

    return [min(lista_de_numeros), max(lista_de_numeros), sum(lista_de_numeros)]

#Programa principal
lista_de_inteiros =[]
tamanho_conjunto = valida_conjunto("Digite a quantidade de elementos que você deseja inserir: ")
while len(lista_de_inteiros) < tamanho_conjunto:
        lista_de_inteiros.append(valida_conjunto("Digite um valor para o conjunto: "))
print("\n Você já digitou todos os valores da sua lista.")
lista_resultado = calcula_maior_menor_soma(lista_de_inteiros)
print(f" O menor valor da lista N é: {lista_resultado[0]}")
print(f" O maior é: {lista_resultado[1]}")
print(f" A soma é:{lista_resultado[2]}")


