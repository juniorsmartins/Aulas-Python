lista_Itens = ['a', 'b', 'c'] #Lista Criada

for itens in lista_Itens: #for para imprimir itens da lista
  print (itens)

lista_Itens.append('d')
lista_Itens.extend(['e', 'f', 'g'])

for itens in lista_Itens:
  print (itens)

print ("Resultado final: {}, {}, {}, {}, {}, {}, {}.".format(lista_Itens[0], lista_Itens[1], lista_Itens[2], lista_Itens[3], lista_Itens[4],
lista_Itens[5], lista_Itens[6]))

lista_Itens.extend(['h', 'i', 'j'])

for i, itens in enumerate(lista_Itens):
  print (i + 1, '=>', itens)

