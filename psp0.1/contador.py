from sys import argv

arquivo = open(argv[1])

def contaLinhasTotais():
  return arquivo.readlines()
#end-function

def contaLinhasDeFuncoes(linhas):
  contador = 0
  i = 0
  inicio = -1
  aux = 0
  for linha in linhas:
    print(linha)
    if (linha[0:3] == 'def') and (aux != -1):
      inicio = i
      aux = -1

    if linha[0:13] == '#end-function':
      contador += (i+1 - inicio)
      inicio = -1
      aux = 0

    i += 1
  
  return contador
#end-function

def contaLinhasEmBranco(linhas):
  contador = 0
  for linha in linhas:
    if (linha[0] == '\n'):
      contador += 1
 
  return contador
#end-function

def escreveSaida(quantidadeLinhas, quantidadeLinhasFuncoes, quantidadeLinhasGlobais, quantidadeLinhasEmBranco):
  print("Linhas totais do arquivo: ", quantidadeLinhas)
  print("- Linhas globais (com conteudo): ", quantidadeLinhasGlobais)
  print("- Linhas referentes a funcoes: ", quantidadeLinhasFuncoes)
  print("- Linhas em branco: ", quantidadeLinhasEmBranco)
# end-function

linhas = contaLinhasTotais()
qtdLinhasDeFuncoes = contaLinhasDeFuncoes(linhas)
qtdLinhasEmBranco = contaLinhasEmBranco(linhas)

print("Analisando arquivo", argv[1])
print("")
escreveSaida(len(linhas), qtdLinhasDeFuncoes, len(linhas)-qtdLinhasDeFuncoes-qtdLinhasEmBranco, qtdLinhasEmBranco)