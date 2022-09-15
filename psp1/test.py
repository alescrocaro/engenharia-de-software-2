import regressaoLinear


# ###################### CASO DE TESTE 1 ######################

xk = 386
x = [130, 650, 99, 150, 128, 302, 95, 945, 368, 961]
y = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]

# ###################### CASO DE TESTE 2 ######################
# n = 10
# x = [130, 650, 99, 150, 128, 302, 95, 945, 368, 961]
# y = [15, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2]


# ###################### CASO DE TESTE 3 ######################
# n = 10
# x = [163, 765, 141, 166, 137, 355, 136, 1206, 433, 1130]
# y = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]

# ###################### CASO DE TESTE 4 ######################
# n = 10
# x = [163, 765,  141, 166,  137,  355,  136,  1206,  433,  1130]
# y = [15,  69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2]


def test_b0_dadosCertos():
    n = 10
    data = regressaoLinear.calcula_yk(x, y, n)
    b0 = data[1] 
    b0 = round(b0, 4)
    assert b0 == -22.5525
#end-function

def test_b1_dadosCertos():
    n = 10
    data = regressaoLinear.calcula_yk(x, y, n)
    b1 = data[2] 
    b1 = round(b1, 6)
    assert b1 == 1.727932
#end-function

def test_yk_dadosCertos():
    n = 10
    data = regressaoLinear.calcula_yk(x, y, n)
    yk = data[0] 
    yk = round(yk, 4)
    assert yk == 644.4294
#end-function

def test_yk_nMenorTamXouY():
    n = 9
    data = regressaoLinear.calcula_yk(x, y, n)
    assert data == None
#end-function

def test_yk_nIgual0():
    n = 0
    data = regressaoLinear.calcula_yk(x, y, n)
    assert data == None
#end-function

def test_yk_nMenor0():
    n = -8
    data = regressaoLinear.calcula_yk(x, y, n)
    assert data == None
#end-function

def test_rxy_dadosCertos():
    n = 10
    data = regressaoLinear.calcula_r(x, y, n)
    rxy = data[0] 
    rxy = round(rxy, 4)
    assert rxy == 0.9545
#end-function

def test_r2_dadosCertos():
    n = 10
    data = regressaoLinear.calcula_r(x, y, n)
    r2 = data[1] 
    r2 = round(r2, 4)
    assert r2 == 0.9111
#end-function

def test_r2_nMenorTamXouY():
    n = 9
    data = regressaoLinear.calcula_r(x, y, n)
    assert data == None
#end-function

# def test_n():
#     n = 0
#     dados = calculaDados(x, y, n, xk)
#     assert dados == False
# #end-function