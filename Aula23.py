# coding: latin-1

calendario = {1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}
aniversario = {1: 'Mário', 2: 'Pedro', 3: 'Gustavo', 4: 'Altair', 5: 'Joaquim', 6: 'Alfredo', 7: 'Manoel', 8: 'Eduardo', 9: 'João', 10: 'Antônio', 11: 'Alexandre', 12: 'Camilo'}
auxiliar = {}

print(calendario)
print("\n")
print(aniversario)
print("\n")
print("Inverter Dicionários")
for itens in range(1, 13):
  auxiliar[itens] = calendario[itens]
  calendario[itens] = aniversario[itens]
  aniversario[itens] = auxiliar[itens]
print("Calendário")
print(calendario)
print("\n")
print("Aniversariantes")
print(aniversario)
