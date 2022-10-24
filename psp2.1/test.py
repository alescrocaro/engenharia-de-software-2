from main import *

# ###################### CASO DE TESTE 1 ######################
def test_busca_x_1():
    p = 0.2
    dof = 6
    data = busca_x(dof, p)
    assert data == None
#end-function

# ###################### CASO DE TESTE 2 ######################

def test_busca_x_2():
    p = 0.45
    dof = 15
    data = busca_x(dof, p)
    data = round(data, 5)
    assert data == 1.75305
#end-function

# ###################### CASO DE TESTE 3 ######################

def test_busca_x_3():
    p = 0.495
    dof = 4
    data = busca_x(dof, p)
    data = round(data, 5)
    assert data == 2
#end-function
