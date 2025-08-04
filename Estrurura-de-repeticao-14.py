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

lista_numeros = []
for i in range(1,11):
    mensagem = f"Digite o {i}° número: "
    lista_numeros.append(valida_entrada(mensagem))

paridade = calcula_paridade(lista_numeros)

pares = [numero for numero in lista_numeros if numero % 2 == 0]
impares = [numero for numero in lista_numeros if numero % 2 != 0]

print(f"Quantidade de números pares: {paridade['Par']}: {pares}")
print(f"Quantidade de números impares: {paridade['Ímpar']}: {impares}")





