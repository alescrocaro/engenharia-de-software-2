import math

def f(x):
  primeiraparte = (math.gamma((dof+1)/2)) / (((dof*(math.pi))**(0.5)) * math.gamma(dof/2))
  teste = dof + 1
  segundaparte = (1 + ((x**2)/dof)) ** (-teste/2)
  result = primeiraparte * segundaparte

  # result = round(result, 5)
  acha.append(result)

  return result
#end-function

def integral(num_seg, w):
  soma1 = 0
  for i in range(1, num_seg, 2):
    soma1 = soma1 + 4*f(i*w)

  soma2 = 0
  for j in range(2, num_seg-1, 2):
    soma2 = soma2 + 2*f(j*w)

  p = (w/3) * ((f(0)) + (soma1) + (soma2) + (f(x)))
  return p
#end-function

def simpson(num_seg):
  erro = math.inf
  result = 0

  while(erro > e):
    integral1 = integral(num_seg, x/num_seg)
    num_seg = num_seg*2
    integral2 = integral(num_seg, x/num_seg)
    result = integral2
    erro = integral1 - integral2
    print('ERRO: ', erro)

  return result
#end-function

num_seg = 10
x = 1.1
e = 0.00001
dof = 9
acha = []
print('RESULTADO: ', simpson(num_seg))