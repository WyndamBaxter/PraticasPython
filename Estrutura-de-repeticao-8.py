def valida_entrada(mensagem):
  '''
  função que valida a entrada do usuário.
  Args:
    mensagem: mensagem que será exibida ao usuário.
  Returns:
    entrada: entrada do usuário.
  '''
  while True:
    try:
      entrada = float(input(mensagem))
      return entrada
    except ValueError as ve:
      print(f"Entrada inválida. Por favor digite um NÚMERO. {ve}")

def calcula_media(lista):
  '''
  função que calcula a média de uma lista de números.
  Args:
    lista: lista de números.
  Returns:
    media: média dos números da lista.
  '''
  soma = sum(lista)
  media = soma / len(lista)
  return media
def calcula_soma(lista):
  '''
  função que calcula a soma de uma lista de números.
  Args:
    lista: lista de números.
  Returns:
    soma: soma dos números da lista.
  '''
  soma = sum(lista)
  return soma

dados_numeros = {}
numeros = [
    ("numero1",valida_entrada, "Digite o número 1"),
    ("numero2",valida_entrada, "Digite o número 2"),
    ("numero3",valida_entrada, "Digite o número 3"),
    ("numero4",valida_entrada, "Digite o número 4"),
    ("numero5",valida_entrada, "Digite o número 5")
]
for campo, funcao_validacao, mensagem in numeros:
    dados_numeros[campo] = funcao_validacao(mensagem)
lista_de_numeros = list(dados_numeros.values())
media = calcula_media(lista_de_numeros)
soma = calcula_soma(lista_de_numeros)
print(f"A média dos números é: {media} e a soma é: {soma}")


