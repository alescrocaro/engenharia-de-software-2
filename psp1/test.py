import regressaoLinear


xk = 386
x = [130, 650, 99, 150, 128, 302, 95, 945, 368, 961]
y = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]

def test_b1():
    n = 10
    b1 = regressaoLinear.calcula_b1(x, y, n)
    b1 = round(b1, 6)
    assert b1 == 1.727932
#end-function

def test_b1_n0():
    n = 0
    b1 = regressaoLinear.calcula_b1(x, y, n)
    assert b1 == None
#end-function

# def test_n():
#     n = 0
#     dados = calculaDados(x, y, n, xk)
#     assert dados == False
# #end-function