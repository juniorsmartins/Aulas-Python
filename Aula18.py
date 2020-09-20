print("")
print("Exercício da Tabuada")
print("")
valor_Digitado = int(input("Digite um valor qualquer para a tabuada? "))
contador = 1
print("")

print("-" * 15)
while contador <= 10:
  print("{:2} x {} = {}".format(contador, valor_Digitado, (contador * valor_Digitado)))
  contador += 1
print("-" * 15)

print("")
print("Finished!")
print("")
