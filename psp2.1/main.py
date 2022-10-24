from simpson import *

def verifica_resultado(esperado, obtido, e):
  if (not esperado): return None
  if (not obtido): return None
  if (not e): return None
  
  diferenca =  esperado - obtido
  
  if diferenca == 0: 
    return 'aceitavel'

  elif diferenca > 0: # esperado > obtido
    if diferenca > e:
      return 'baixo' # deve realizar passo 3 ou 6

    return 'aceitavel' # chegou no resultado esperado ou proximo dele

  elif diferenca < 0: # esperado < obtido
    diferenca = diferenca * -1

    if diferenca > e:
      return 'alto' # deve realizar passo 4 ou 7

    return 'aceitavel' # chegou no resultado esperado ou proximo dele
#end-function

def ajustar_x(x, d, flag_diferenca):
  if (x < 0): return None
  if (d == 0): return x
  if (d < 0): return None
  if (not flag_diferenca): return None

  if flag_diferenca == 'baixo': # resultado eh muito baixo
    return x + d

  elif flag_diferenca == 'alto': # resultado eh muito baixo
    return x - d
#end-function

def ajustar_d(erro, d):
  if (not erro): return None
  if (not d): return None

  if erro >= 0:
    return d

  return d/2
#end-function

def busca_x(dof, p):
  if (not dof): return None

  e = 0.00001
  x = 1
  d = 0.5
  i = 0

  result, erro = simpson(x, e, dof)
  flag_diferenca = verifica_resultado(p, result, e)
  if flag_diferenca == 'aceitavel': 
    return x
  x = ajustar_x(x, d, flag_diferenca)

  while True:
    result, erro = simpson(x, e, dof)

    flag_diferenca = verifica_resultado(p, result, e)
    if flag_diferenca == 'aceitavel': 
      return x
    d = ajustar_d(erro, d)
    x = ajustar_x(x, d, flag_diferenca)

    # sleep(0.2)
    i = i+1
    if(d <= 0): return x
    if(i > 100000): return None
#end-function
