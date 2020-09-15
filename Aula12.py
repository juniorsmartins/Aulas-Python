# -*- coding: utf-8 -*-
print('')
print('Estudo de Python')
print('Livro: Python para desenvolvedores - Luiz Eduardo Borges')
print('')

nome = input('Qual teu nome? ')
nota1 = float(input('Qual tua primeira nota? '))
nota2 = float(input('Qual tua segunda nota? '))
nota3 = float(input('Qual tua terceira nota? '))
nota_media = (nota1 + nota2 + nota3)/3

if nota_media < 0:
  print('Nota c/ Erro!')
elif 0 <= nota_media < 7:
  print('Reprovado!')
elif 7 <= nota_media < 9: 
  print('Aprovado!')
elif 9 <= nota_media <= 10:
  print('Aprovado com louvor!')
else: 
  print('Nota inexistente!')
