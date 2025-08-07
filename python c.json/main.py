import json

#FIZ DUPLA COM O PAULO

ARQUIVO_CADASTRO = "cadastros.json"

def exibir_menu():
    print("\n==== MEnu =========")
    print("1. Cadastrar pessoa")
    print("2. Ver cadastros")
    print("3. Sair")
    print("=====================")

def salvar_cadastros(cadastros):
    with open(ARQUIVO_CADASTRO, "w", encoding="utf-8") as arquivo:
              json.dump(cadastros, arquivo, indent=4, ensure_ascii=False)

def carregar_cadastros():
      try:
            with open(ARQUIVO_CADASTRO, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

def cadastrar_pessoa(cadastros):
      nome = input("Nome: ")
      idade = input("idade: ")
      turma = input("Turma: ")
      curso = input("Curso: ")

      cadastros.appends({"Nome": nome, "Idade": idade, "Turma": turma, "Curso": curso})
      salvar_cadastros(cadastros)
      print("Cadastro realizado com sucesso!")

def ver_cadastros(cadastros):
      if not cadastros:
            print("\nNehum cadastro realizado.")
      else:
          print("\n==== LISTA DE CADASTROS ======")
          for i, pessoa in enumerate(cadastros, 1):
                print(f"{i}. Nome: {pessoa['Nome']}, Idade: {pessoa ['Idade']}, Turma: {pessoa['Turma']}, Curso: {pessoa['Curso']}" input ("\nPressione Enter para voltar ao menu..."))