# coding: latin-1

breakfest = {1:'leite', 2:'café', 3:'pão', 4:'manteiga', 5:'queijo', 6:'presunto', 7:'granola'}
print(breakfest)

for itens in breakfest:
  print(itens, breakfest[itens])

print(" ")
breakfest[6] = 'mortadela'

for itens in breakfest:
  print(itens, breakfest[itens])
