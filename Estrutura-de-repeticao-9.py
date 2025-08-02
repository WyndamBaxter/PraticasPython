def valida_entrada(mensagem):
  '''
  Função que valida a entrada do usuário.
  Args:
    mensagem: Mensagem que será exibida ao usuário.
  Returns:
    entrada: Entrada do usuário.
  '''
  while True:
    try:
      entrada = int(input(mensagem))
      return entrada
    except ValueError:
      print('Entrada inválida. Por favor digite um número inteiro válido!.')
    except Exception as e:
      print(f'Ocorreu um erro desconhecido: {e}')
def gera_intervalo(inicio, fim):
  '''
  Função que gera um intervalo de números inteiros.
  Args:
    inicio: Número inicial do intervalo.
    fim: Número final do intervalo.
  Returns:
    intervalo: Lista com os números inteiros no intervalo.
  '''
  intervalo = []
  for inteiro in range(inicio, fim + 1 ):
    intervalo.append(inteiro)
  return intervalo
#programa principal
dados_intervalo = {}
lista_intervalo = [
    ("numero1", valida_entrada, "Digite o número inicial do intervalo:"),
    ("numero2", valida_entrada, "Digite o número final do intervalo:")
]
for campo, funcao_validacao, mensagem in lista_intervalo:
  dados_intervalo[campo] = funcao_validacao(mensagem)

intervalo = gera_intervalo(dados_intervalo["numero1"], dados_intervalo["numero2"])
print(f"Os números inteiros desse intervalo são: {intervalo}")