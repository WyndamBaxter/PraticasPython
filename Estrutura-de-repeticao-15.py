'''
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa
 capaz de gerar a série até o n−ésimo termo.
'''
def valida_entrada(mensagem):
    '''
    Função que valida a entrada do usuário.
    :param mensagem: recebe mensagem do usuário
    :return: entrada: retorna o valor digitado pelo usuário.
    '''
    while True:
        try:
            entrada = int(input(mensagem))
            if 1 <= entrada:
                return entrada
            else:
                print(f"Entrada inválida, por favor digite um inteiro maior ou igual a 1.")
        except ValueError as ve:
            print(f"Entrada inválida, por favor digite um número inteiro maior ou igual a 1.{ve}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
def calcula_sequencia(termos):
    '''
    Função que calcula a sequência de fibonacci.
    :param numero: Recebe inteiro para calcular
    :return: sequencia_de_fibonacci: lista com a sequência até um valor "n".
    '''
    sequencia_de_fibonacci = [1, 1]
    while len(sequencia_de_fibonacci) < termos:
        valor_sequencia = sequencia_de_fibonacci[-1] + sequencia_de_fibonacci[-2]
        sequencia_de_fibonacci.append(valor_sequencia)

    return sequencia_de_fibonacci
lista = valida_entrada("Digite numero: ")
sequencia_fibonacci = calcula_sequencia(lista)
print(sequencia_fibonacci)


