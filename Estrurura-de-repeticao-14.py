'''
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números
pares e a quantidade de números impares.
'''
def valida_entrada(mensagem):
    '''
    Função de validação de entrada
    Args:
        mensagem: mensagem recebida do usuário.
    Returns:
        entrada: retorna o valor da mensagem.
    '''
    while True:
        try:
            entrada = int(input(mensagem))
            if entrada > 0:
                return entrada
            else:
                print(f"Entrada inválida, por favor digite um inteiro maior que zero.")
        except ValueError as e:
            print(f"Entrada inválida, por favor digite um número inteiro. {e}")
        except Exception as ve:
            print(f"Ocorreu um erro inesperado: {ve}")
def calcula_paridade(lista_numeros):
    '''
    Função que calcula paridade do numero dado.
    Args:
        lista_de_numeros: numero dado pelo usuário.
    Returns:
        paridade: Dicionário com valores chave-valor contendo os resultados de paridade-numero.
    '''
    paridade_contagem = {"Par": 0, "Ímpar": 0}

    for numero in lista_numeros:
        if numero % 2 == 0:
            paridade_contagem["Par"] += 1
        else:
            paridade_contagem["Ímpar"] += 1

    return paridade_contagem


lista_de_validacao = [
    ("numero1", valida_entrada, "Digite o primeiro número"),
    ("numero2", valida_entrada, "Digite o segundo número"),
    ("numero3", valida_entrada, "Digite o terceiro número"),
    ("numero4", valida_entrada, "Digite o quarto número"),
    ("numero5", valida_entrada, "Digite o quinto número"),
    ("numero6", valida_entrada, "Digite o sexto número"),
    ("numero7", valida_entrada, "Digite o sétimo número"),
    ("numero8", valida_entrada, "Digite o oitavo número"),
    ("numero9", valida_entrada, "Digite o nono número"),
    ("numero10", valida_entrada, "Digite o décimo número")
]
#Loop para entrada do usuário.
lista_numeros = []
for campo, funcao_validacao, mensagem in lista_de_validacao:
    lista_numeros.append(funcao_validacao(mensagem))
#Dicionário contendo a contagem de valores pares e ímpares retornadas pela função calcula_paridade.
paridade = calcula_paridade(lista_numeros)
#Impressão da quantidade de ímpares e pares

pares = [numero for numero in lista_numeros if numero % 2 == 0]
impares = [numero for numero in lista_numeros if numero % 2 != 0]
print(f"Quantidade de números pares: {paridade['Par']}: {pares}")
print(f"Quantidade de números impares: {paridade['Ímpar']}: {impares}")





