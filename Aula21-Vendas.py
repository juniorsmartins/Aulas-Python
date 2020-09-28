# coding: latin-1

cad_Prod[] = dict()
cad_Prod['codigo'] = 0;

opcao_Principal = 8
while (opcao_Principal != 0):
  print("\n"*5)
  print("-"*40)
  print("-"*15 + "   Menu   " + "-"*15)
  print("-"*40)
  print("-"*13 + "  Vender - 1  " + "-"*13)
  print("-"*11 + "  Consultar - 2  " + "-"*12)
  print("-"*11 + "  Cadastrar - 3  " + "-"*12)
  print("-"*12 + "  Alterar - 4  " + "-"*13)
  print("-"*12 + "  Excluir - 5  " + "-"*13)
  print("-"*12 + "  Relatar - 6  " + "-"*13)
  print("-"*14 + "  Sair - 0  " + "-"*14)
  print("-"*40)
  opcao_Principal = int(input("-"*10 + "  Qual opção? "))

  if (opcao_Principal == 1):
    print("\n")
    print("Vender - 1")
    input("Digite <enter> para continuar...")
  elif (opcao_Principal == 2):
    print("\n")
    print("Consultar - 2")
    print("\n")
    print(cad_Prod)
    input("Digite <enter> para continuar...")
  elif (opcao_Principal == 3):

    print("\n")
    cad_Prod['nome'] = str(input('Nome: '))
    cad_Prod['custo'] = float(input('Custo: '))
    cad_Prod['quantia'] = float(input('Quantia: '))
    cad_Prod['lucro'] = float(input('Markup: '))
    cad_Prod['codigo'] = cad_Prod['codigo'] + 1
    print("\n")
    print("Cadastrar - 3")
    input("Digite <enter> para continuar...")


  elif (opcao_Principal == 4):
    print("\n")
    print("Alterar - 4")
    input("Digite <enter> para continuar...")
  elif (opcao_Principal == 5):
    print("\n")
    print("Excluir - 5")
    input("Digite <enter> para continuar...")
  elif (opcao_Principal == 6):
    print("\n")
    print("Relatar - 6")
    input("Digite <enter> para continuar...")
  elif (opcao_Principal == 0):
    print("\n")
    print("Sair - 0")
    input("Digite <enter> para continuar...")
  else:
    print("\n")
    print("Opção Inválida!")
    input("Digite <enter> para continuar...")

else:
  print("\n")
  print("Tchau! Hasta la vista baby.")
  print("\n")

