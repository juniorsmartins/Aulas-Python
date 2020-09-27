print('')
print('Estudo de Python')
print('Livro: Tutorial de Introdução ao Python - Pet Tele')
print('')

meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

while 1: 
  mes = int(input('Digite um mês de 1 a 12: '))
  if 1 <= mes <= 12: 
    print('')
    print('O mês escolhido é: {}'.format(meses[mes - 1]))
    print('')
