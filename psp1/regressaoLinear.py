import math

def calcula_xTotal(x, n):
    # if (n <= 0): return None
    # if (len(x) != n): return None

    xTotal = 0
    for i in range(n):
        xTotal = xTotal + x[i]

    return xTotal
#end-function

def calcula_yTotal(y, n):
    # if (n <= 0): return None
    # if (len(y) != n): return None

    yTotal = 0
    for i in range(n):
        yTotal = yTotal + y[i]

    return yTotal
#end-function

def calcula_somatoriaXY(x, y, n):
    # if (n <= 0): return None
    # if (len(x) != len(y)): return None
    # if (len(x) != n): return None
    # if (len(y) != n): return None

    soma = 0
    for i in range(n):
        soma = soma + x[i]*y[i]

    return soma
#end-function

def calcula_xQuad(x, n):
    xQuad = 0
    for i in range(n):
        xQuad = xQuad + x[i]**2

    return xQuad
#end-function

def calcula_yQuad(y, n):
    yQuad = 0
    for i in range(n):
        yQuad = yQuad + y[i]**2

    return yQuad
#end-function

def calcula_xAvg(xTotal, n):
    return xTotal/n
#end-function

def calcula_yAvg(yTotal, n):
    return yTotal/n
#end-function

def calcula_b1(x, y, n):
    if(n <= 0): return None

    xTotal = calcula_xTotal(x, n)
    xAvg = calcula_xAvg(xTotal, n)

    yTotal = calcula_yTotal(y, n)
    yAvg = calcula_yAvg(yTotal, n)

    xQuad = calcula_xQuad(x, n)
    yQuad = calcula_yQuad(y, n)

    somatoria_xy = calcula_somatoriaXY(x, y, n)

    b1 = ((somatoria_xy - (n * xAvg * yAvg))/(xQuad - (n * (xAvg**2))))

    return b1
#end-function

def calcula_b0(b1, xAvg, yAvg):
    return (yAvg - (b1*xAvg))
#end-function

def calcula_rxy(n, xTotal, yTotal, xQuad, yQuad,):
    return((n*somatoria_xy) - (xTotal*yTotal))/(math.sqrt((n * xQuad - (math.pow(xTotal, 2))) * (n * yQuad - (math.pow(yTotal, 2)))))
#end-function

def calcula_rQuad(rxy):
    return rxy**2
#end-function

def calcula_yk(b0, b1, xk = 386):
   return b0 + (b1*xk)
#end-function

###################### CASO DE TESTE 1 ######################
n = 10
x = [130, 650, 99, 150, 128, 302, 95, 945, 368, 961]
y = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]

###################### CASO DE TESTE 2 ######################
n = 10
x = [130, 650, 99, 150, 128, 302, 95, 945, 368, 961]
y = [15, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2]


###################### CASO DE TESTE 3 ######################
n = 10
x = [163, 765, 141, 166, 137, 355, 136, 1206, 433, 1130]
y = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]

###################### CASO DE TESTE 4 ######################
n = 10
x = [163, 765,  141, 166,  137,  355,  136,  1206,  433,  1130]
y = [15,  69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2]

