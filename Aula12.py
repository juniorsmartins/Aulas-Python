# -*- coding: utf-8 -*-

print('')
print('Estudo de Python')
print('Livro: Python para desenvolvedores - Luiz Eduardo Borges')
print('')

nome = input('Qual teu nome? ')
nota1 = float(input('Qual tua primeira nota? '))
nota2 = float(input('Qual tua segunda nota? '))
nota3 = float(input('Qual tua terceira nota? '))
media = (nota1 + nota2 + nota3)/3

if 0 <= media < 7:
  print 'Reprovado!'
elif 7 <= media < 9: 
  print 'Aprovado!'
elif 9 <= media <= 10:
  print 'Aprovado com louvor!'
else: 
  print 'Nota inexistente!'
