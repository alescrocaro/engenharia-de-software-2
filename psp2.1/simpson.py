import math

def f(x, dof):
  primeiraparte = (math.gamma((dof+1)/2)) / (((dof*(math.pi))**(0.5)) * math.gamma(dof/2))
  teste = dof + 1
  segundaparte = (1 + ((x**2)/dof)) ** (-teste/2)
  result = primeiraparte * segundaparte

  return result
#end-function

def integral(x, num_seg, w, dof):
  soma1 = 0
  for i in range(1, num_seg, 2):
    soma1 = soma1 + 4*f(i*w, dof)

  soma2 = 0
  for j in range(2, num_seg-1, 2):
    soma2 = soma2 + 2*f(j*w, dof)

  p = (w/3) * ((f(0, dof)) + (soma1) + (soma2) + (f(x, dof)))
  return p
#end-function

def simpson(x, e, dof, num_seg = 10):
  erro = math.inf
  result = 0

  while(erro > e):
    integral1 = integral(x, num_seg, x/num_seg, dof)
    num_seg = num_seg*2
    integral2 = integral(x, num_seg, x/num_seg, dof)
    result = integral2
    erro = integral1 - integral2

  return result, erro
#end-function
