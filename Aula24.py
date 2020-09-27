# coding: latin-1

for contador in range (5, 0, -1):
  print(contador)
print("\n")

for cont in range (1, 6):
  print(cont)
print("\n")

lista = {1, 4, 7, 9}
for itens in lista:
  print(itens)
print("\n")

arquivo = {1: "Mário", 2: "Pedro", 3: "Alberto", 4: "Francisco"}
for itens in arquivo:
  print(itens, arquivo[itens])
print("\n")

ferramentas = {1: "Martelo", 2: "Prego", 3: "Alicate", 4: "Serrote"}
for itens, valor in ferramentas.items():
  print(itens, " -> ", valor)
print("\n")
