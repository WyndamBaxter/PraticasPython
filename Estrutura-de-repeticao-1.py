#função de validação de entrada do usuário
def valida_entrada(mensagem):
  '''
  Função de validação de entrada do usuário
  Args:
    mensagem: mensagem a ser exibida ao usuário
  Returns:
    entrada: entrada do usuário
  '''
  while True:
    try:
      entrada = int(input(mensagem))
      if 0 <= entrada <= 10:
        return entrada
      else:
        print("Favor digite um número válido!")
    except ValueError as ve:
      print(f"Favor digitar um número entre 1 e 10: {ve}")
    except Exception as e:
      print(f"Ocorreu um erro inesperado: {e}")
#Programa principal
nota = valida_entrada("Digite uma nota entre 1 e 10: ")
print(f"A nota digitada foi: {nota}")