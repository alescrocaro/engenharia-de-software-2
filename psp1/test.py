from regressaoLinear import calculaDados

n = 10
xk = 386
x = [130, 650, 99, 150, 128, 302, 95, 945, 368, 961]
y = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]

def test_b1():
    dados = calculaDados(x, y, n, xk)
    b1 = dados[0]
    b1 = round(b1, 6)
    assert b1 == 1.727932
#end-function