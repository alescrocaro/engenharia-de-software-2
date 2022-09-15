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

def calcula_yk(x, y, n,  xk = 386):
    if(n <= 0): return None
    if (len(x) != len(y)): return None
    if (len(x) != n): return None

    xTotal = calcula_xTotal(x, n)
    xAvg = calcula_xAvg(xTotal, n)

    yTotal = calcula_yTotal(y, n)
    yAvg = calcula_yAvg(yTotal, n)

    xQuad = calcula_xQuad(x, n)

    somatoria_xy = calcula_somatoriaXY(x, y, n)

    b1 = (somatoria_xy - (n * xAvg * yAvg))/(xQuad - (n * (xAvg**2)))
    b0 = yAvg - (b1*xAvg)
    yk = b0 + (b1*xk)

    return yk, b0, b1
#end-function

def calcula_r(x, y, n):
    if(n <= 0): return None
    if (len(x) != len(y)): return None
    if (len(x) != n): return None
    if (len(y) != n): return None

    xTotal = calcula_xTotal(x, n)
    yTotal = calcula_yTotal(y, n)

    xQuad = calcula_xQuad(x, n)
    yQuad = calcula_yQuad(y, n)

    somatoria_xy = calcula_somatoriaXY(x, y, n)

    
    rxy = ((n*somatoria_xy) - (xTotal*yTotal))/(math.sqrt((n * xQuad - (math.pow(xTotal, 2))) * (n * yQuad - (math.pow(yTotal, 2)))))
    r2 = rxy**2
    
    return rxy, r2
#end-function
