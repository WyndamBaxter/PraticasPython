def valida_entrada(mensagem):
  '''
  Função que valida a entrada do usuário.
  Args:
    mensagem: Mensagem que será exibida na tela.
  Returns:
    valor: Valor digitado pelo usuário.
  '''
  while True:
    try:
      valor = float(input(mensagem))
      return valor
    except ValueError:
      print("Entrada inválida. Por favor, digite um número.")

dados_numeros ={}
numeros =[
    ("numero1", valida_entrada, "Digite o primeiro número:"),
    ("numero2", valida_entrada, "Digite o segundo número:"),
    ("numero3", valida_entrada, "Digite o terceiro número:"),
    ("numero4", valida_entrada, "Digite o quarto número:"),
    ("numero5", valida_entrada, "Digite o quinto número:"),
]
for campos, funcao_validacao, mensagem in numeros:
  dados_numeros[campos] = funcao_validacao(mensagem)

maior_numero = max(dados_numeros.values())
print(f"O maior número é: {maior_numero}")

