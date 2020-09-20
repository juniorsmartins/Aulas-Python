print("")
quantia = int(input("Quantas notas quer calcular? "))
print("")
nota = soma = 0
contador = 1

while contador <= quantia :
  nota = float(input("Digite sua nota? "))
  soma = (soma + nota)
  contador += 1

media = float(soma / quantia)

print("")
print("Sua média é: {:.1f}".format(media))
print("")
