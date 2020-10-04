lista = ['A', 'B', 'C']

for i, itens in enumerate(lista):
  print (i + 1, ' = ', itens)

lista[-1] = 'D'
lista[-2] = 'F'
lista[-3] = 'M'

for e, itens in enumerate(lista):
  print (e + 1, ' -> ', itens)

lista.remove('F')

for d, itens in enumerate(lista):
  print(d + 1, ' == ', itens)

lista.extend(['B', 'C', 'A'])
lista.sort()

for f, itens in enumerate(lista):
  print(f + 1, ' === ', itens)

lista.reverse()

for a, itens in enumerate(lista):
  print(a + 1, '//', itens)
