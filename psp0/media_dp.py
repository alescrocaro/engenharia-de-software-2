import statistics

def media(listaNumeros):
  return statistics.mean(listaNumeros)

def dp(listaNumeros):
  return statistics.pstdev(listaNumeros)

qtdNumeros = input('Quantos numeros deseja inserir?')
qtdNumeros = int(qtdNumeros)

listaNumeros = []

for _ in range(qtdNumeros):
  listaNumeros.append(0)
  
i=0
for i in range(qtdNumeros):
  listaNumeros[i] = input('Digite um numero: ')
  listaNumeros[i] = float(listaNumeros[i])

print('\n')
print('media: ', media(listaNumeros))
print('dp: ', dp(listaNumeros))
