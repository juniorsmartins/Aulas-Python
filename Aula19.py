# -*- coding: latin1 -*-
import random

print("")
print("Linguagem de Programação Python!")
print("Aprendendo Python")
print("")
print("Programa - Tente acertar o número sorteado")
print("")
valor_Sorteado = random.randint(1, 10)
valor_Escolhido = 0

while valor_Escolhido != valor_Sorteado :
  print("")
  valor_Escolhido = int(input("Digite um número inteiro de 0 até 10: "))
  print("")
  if valor_Escolhido == valor_Sorteado :
    print("Você acertou!")
    print("")
  elif (valor_Escolhido != valor_Sorteado):
    print("Você errou!")
    print("Tente novamente!")
    print("")
    input("Tecle <enter> para continuar!")
    print("")
