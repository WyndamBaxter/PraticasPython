
def valida_entrada(mensagem):
  '''
  Função que valida a entrada do usuário.
  Args:
    mensagem: Mensagem a ser exibida ao usuário.
  Returns:
    populacao: População inicial dada pelo usuário.
  '''
  while True:
    try:
      populacao = int(input(mensagem))
      if populacao > 0:
        return populacao
      else:
        print("Valor digitado inválido. Por favor digite um número maior que zero.")
    except ValueError as ve:
      print("Valor digitado inválido. Por favor digite um número inteiro.")

def calcula_anos_necessarios(populacao_a, populacao_b, taxa_crescimento_a, taxa_crescimento_b):
  '''
  Função que calcula o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
  Args:
    populacao_a: População inicial do país A
    populacao_b: População inicial do país B
    taxa_crescimento_a: Taxa de crescimento do país A
    taxa_crescimento_b: Taxa de crescimento do país B
  Returns:
    anos: Número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
  '''
  anos = 0
  while populacao_a < populacao_b:
    populacao_a += populacao_a * taxa_crescimento_a
    populacao_b += populacao_b * taxa_crescimento_b
    anos += 1
  return anos

#PROGRAMA PRINCIPAL
TAXA_CRESCIMENTO_A = 0.03
TAXA_CRESCIMENTO_B = 0.015
dados_cidade = {}
populacao = [
    ("populacao_a", valida_entrada, "Digite a população da cidade A: "),
    ("populacao_b", valida_entrada, "Digite a população da cidade B: ")
]
for campo, funcao_validacao, mensagem in populacao:
  dados_cidade[campo] = funcao_validacao(mensagem)

anos = calcula_anos_necessarios(dados_cidade["populacao_a"], dados_cidade["populacao_b"], TAXA_CRESCIMENTO_A, TAXA_CRESCIMENTO_B)
print(f"Serão necessários {anos} anos para que a População de A seja igual ou maior que a População da cidade B.")