def valida_nome(mensagem):
  '''
  função que valida o nome de usuário
  Args:
    mensagem: string - Mensagem exibida ao solicitar o nome.
  Returns:
    nome: string - O nome de usuário validado.
  '''
  while True:
    nome = input(mensagem).strip()
    if nome: # Verifica se o nome não está vazio
      return nome
    else:
      print("O nome de usuário não pode ser vazio.")

def valida_senha(mensagem, nome_usuario):
  '''
  função que valida a senha
  Args:
    mensagem: string - Mensagem exibida ao solicitar a senha.
    nome_usuario: string - O nome de usuário para comparação.
  Returns:
    senha: string - A senha validada.
  '''
  while True:
    senha = input(mensagem).strip()
    if senha and senha != nome_usuario: # Verifica se a senha não está vazia e é diferente do nome
      return senha
    elif not senha:
      print("A senha não pode ser vazia.")
    else:
      print("A senha não pode ser igual ao nome de usuário.")

nome = valida_nome("Digite o nome de usuário: ")
senha = valida_senha("Digite sua senha: ", nome)
print(f"Nome de usuário: {nome}")
print(f"Senha: {senha}")