print('Desafio 5 - Curso em Vídeo')
print('Professor: Gustavo Guanabara')
print('Conversões de tipo')

n1 = int(input('Digite um valor inteiro: '))
print(type(n1))
n2 = float(input('Digite um valor real: '))
print(type(n2))
n3 = bool(input('Digite 0 ou 1: '))
print(type(n3))
n4 = str(input('Digite uma frase: '))
print(type(n4))
print('Respostas {}, {}, {}, {}'.format(n1, n2, n3, n4))

print('')
n5 = input('Digite algo: ')
print(n5.isnumeric())
print(n5.isalpha())
print(n5.isalnum())

