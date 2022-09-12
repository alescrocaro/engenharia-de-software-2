import math

def calculaDados(x, y, n, xk, xTotal = 0, xAvg = 0, xQuad = 0, yTotal = 0, yAvg = 0, yQuad = 0, somatoriaXY = 0):
    for i in range(n):
        xTotal = xTotal + x[i]
        yTotal = yTotal + y[i]
        somatoriaXY = somatoriaXY + x[i]*y[i]
        xQuad = xQuad + x[i]**2
        yQuad = yQuad + y[i]**2

    xAvg = xTotal/n
    yAvg = yTotal/n
    
    b1 = (somatoriaXY - (n * xAvg * yAvg))/(xQuad - (n * (xAvg**2)))

    b0 = yAvg - (b1*xAvg)

    p = (n*somatoriaXY) - (xTotal*yTotal)
    q = math.sqrt((n * xQuad - (math.pow(xTotal, 2))) * (n * yQuad - (math.pow(yTotal, 2))))

    rxy = p/q
    r2 = rxy*rxy
    
    yk = b0 + (b1*xk)

    return b1, b0, rxy, r2, yk
#end-function


def test_b1(x, y, n, xk):
    b1 = calculaDados(x, y, n, xk)
    assert b1 == 1.727932
#end-function

########################
print('CASO DE TESTE 1')

n = 10
xk = 386
x = [130, 650, 99, 150, 128, 302, 95, 945, 368, 961]
y = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]

b1, b0, rxy, r2, yk = calculaDados(x, y, n, xk)

test_b1(x, y, n, xk)

print('b1: ', b1)
print('b0: ', b0)
print('rxy: ', rxy)
print('r2: ', r2)
print('yk: ', yk)
print()

########################
print()
print('CASO DE TESTE 2')

y = [15, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2]

b1, b0, rxy, r2, yk = calculaDados(x, y, n, xk)

print('b1: ', b1)
print('b0: ', b0)
print('rxy: ', rxy)
print('r2: ', r2)
print('yk: ', yk)

########################
print()
print('CASO DE TESTE 3')

x = [163, 765, 141, 166, 137, 355, 136, 1206, 433, 1130]
y = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]

b1, b0, rxy, r2, yk = calculaDados(x, y, n, xk)

print('b1: ', b1)
print('b0: ', b0)
print('rxy: ', rxy)
print('r2: ', r2)
print('yk: ', yk)

########################
print()
print('CASO DE TESTE 4')

x = [163, 765,  141, 166,  137,  355,  136,  1206,  433,  1130]
y = [15,  69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2]

b1, b0, rxy, r2, yk = calculaDados(x, y, n, xk)

print('b1: ', b1)
print('b0: ', b0)
print('rxy: ', rxy)
print('r2: ', r2)
print('yk: ', yk)
