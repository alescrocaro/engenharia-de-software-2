from sys import argv

arquivo = open(argv[1])

def contaLinhasTotais():
  return arquivo.readlines()
#end-function

def contaLinhasDeFuncoes(linhas, funcoes):
  qtdLinhas = [0, 0] # posicao1: qtd linhas totais de funcoes; posicao2: qtd linhas funcao atual;
  i = j = 0
  inicio = -1
  aux = 0
  mediaLinhas = 0
  qtdFuncoes = 0
  defineNome = ''

  for linha in linhas:
    if (linha[0:3] == 'def') and (aux != -1):
      inicio = i
      aux = -1
      qtdFuncoes += 1
      defineNome = linha[4:].split('(')

    if linha[0:13] == '#end-function':
      qtdLinhas[0] += (i+1 - inicio)
      qtdLinhas[1] += (i+1 - inicio)

      funcoes.append({'nome': defineNome[0], 'qtdLinhas': qtdLinhas[1]})

      inicio = -1
      aux = 0
      j += 1
      qtdLinhas[1] = 0

    i += 1
  
  mediaLinhas = qtdLinhas[0]/qtdFuncoes

  return qtdLinhas[0], mediaLinhas, funcoes
#end-function

def contaLinhasEmBranco(linhas):
  contador = 0
  for linha in linhas:
    if (linha[0] == '\n'):
      contador += 1
 
  return contador
#end-function

def escreveSaida(quantidadeLinhas, quantidadeLinhasFuncoes, mediaLinhasFuncoes, quantidadeLinhasGlobais, quantidadeLinhasEmBranco, funcoes):
  print("Linhas totais do arquivo: ", quantidadeLinhas)
  print("- Linhas globais (com conteudo): ", quantidadeLinhasGlobais)
  print("- Linhas em branco: ", quantidadeLinhasEmBranco)
  print("- Linhas totais referentes a funcoes: ", quantidadeLinhasFuncoes)
  print("- Média de linhas de funcoes: ", mediaLinhasFuncoes)
  print("- Quantidades de linhas por função: ")
  for i in range(len(funcoes)):
    nome = funcoes[i].get('nome')
    qtdLinhas = funcoes[i].get('qtdLinhas')
    print("\t - " + nome + ": " + str(qtdLinhas))
# end-function

linhas = contaLinhasTotais()
funcoes = []
qtdLinhasDeFuncoes, mediaLinhasFuncoes, infoFuncoes = contaLinhasDeFuncoes(linhas, funcoes)
qtdLinhasEmBranco = contaLinhasEmBranco(linhas)

print("Analisando arquivo", argv[1])
print("")
escreveSaida(len(linhas), qtdLinhasDeFuncoes, mediaLinhasFuncoes, len(linhas)-qtdLinhasDeFuncoes-qtdLinhasEmBranco, qtdLinhasEmBranco, funcoes)