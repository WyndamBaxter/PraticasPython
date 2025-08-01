#CONSTANTES
ESTADO_CIVIL = ["s","c","v","d"]
#-------------------------------------------------------------------------------
def valida_nome(mensagem):
  '''
  Função que valida o nome do usuário.
  Args:
      mensagem: Mensagem que será exibida ao usuário.
  Returns:
      nome: Nome do usuário.
  '''
  while True:
      try:
          nome = input(mensagem).strip()
          if len(nome) > 3:
            return nome
          else:
              print("O nome deve ter pelo menos 3 caracteres.")
      except ValueError as ve:
        print(f"Você digitou um número? Por favor digite seu nome.")
      except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
#-------------------------------------------------------------------------------
def valida_idade(mensagem):
  '''
  Função que valida a idade do usuário.
  Args:
      mensagem: Mensagem que será exibida ao usuário.
  Returns:
      idade: Idade do usuário.
  '''
  while True:
    try:
      idade = int(input(mensagem))
      if 0 <= idade <= 150:
        return idade
      else:
          print("Por favor digite uma idade válida entre 0 e 150 anos.")
    except ValueError as ve:
      print(f"Por favor, digite sua idade em anos (somente números).")
    except Exception as e:
      print(f"Ocorreu um erro inesperado: {e}")
#-------------------------------------------------------------------------------
def valida_salario(mensagem):
  '''
  Função que valida o salário do usuário.
  Args:
      mensagem: Mensagem que será exibida ao usuário.
  Returns:
      salario: Salário do usuário.
  '''
  while True:
    try:
      salario = float(input(mensagem))
      if salario > 0:
        return salario
      else:
        print("O salário deve ser maior que zero.")
    except ValueError as ve:
      print(f"Por favor, digite seu salário em Reais.")
    except Exception as e:
      print(f"Ocorreu um erro inesperado {e}")
#-------------------------------------------------------------------------------
def valida_estado_civil(mensagem):
  '''
  Função que valida o estado civil do usuário.
  Args:
      mensagem: Mensagem que será exibida ao usuário.
  Returns:
      estado_civil: Estado civil do usuário.
  '''
  while True:
    try:
      estado_civil = input(mensagem).strip().lower()
      if estado_civil in ESTADO_CIVIL:
        return estado_civil
      else:
        print("Por favor, digite um estado civil válido: 's - solteiro(a)', 'c - casado(a)', 'v - viúvo(a)', 'd - divorciado(a)'.")
    except ValueError as ve:
      print(f"Por favor, digite um estado civil válido. {ve}")
    except Exception as e:
      print(f"Ocorreu um erro inesperado: {e}")
#-------------------------------------------------------------------------------
def exibe_dados_usuario(nome, idade, salario, estado_civil):
  '''
  Função que exibe os dados do usuário.
  Args:
      nome: Nome do usuário.
      idade: Idade do usuário.
      salario: Salário do usuário.
      estado_civil: Estado civil do usuário.
  Returns:
      None
  '''
  print(f"Nome: {nome}")
  print(f"Idade: {idade}")
  print(f"Salário R$: {salario:.2f}")
  print(f"Estado civil: {estado_civil}")
#Programa principal:
'''
nome = valida_nome("Digite seu nome: ")
idade = valida_idade("Digite sua idade em anos: ")
salario = valida_salario("Digite seu salário em Reais:")
estado_civil = valida_estado_civil("Digite seu estado civil: 's - solteiro(a)', 'c - casado(a)', 'v - viúvo(a)', 'd - divorciado(a)' ")
exibe_dados_usuario(nome, idade, salario, estado_civil)
'''
dados_usuario = {}
campos = [
    ("nome",valida_nome, "Digite seu nome: "),
    ("idade", valida_idade, "Digite sua idade em anos: "),
    ("salario", valida_salario, "Digite seu salário em Reais: "),
    ("estado_civil", valida_estado_civil, "Digite seu estado civil: 's - solteiro(a)', 'c - casado(a)', 'v - viúvo(a)', 'd - divorciado(a)' ")

]
for campo, funcao_validacao, mensagem in campos:
   dados_usuario[campo] = funcao_validacao(mensagem)
exibe_dados_usuario(dados_usuario["nome"], dados_usuario["idade"], dados_usuario["salario"], dados_usuario["estado_civil"])