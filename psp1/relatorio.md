# PSP1 - Programa 3

## Formulário de resumo de planejamento de projeto

- Li o documento de descrição do programa 3
- Procurei por códigos ou bibliotecas de regressão linear em python
- Percebi que seria mais fácil implementar a fórmula que está no documento
- Finalizei definindo os passos que faria para implementar a fórmula (seguindo o exemplo de cálculo contido no documento)

## Modelo de relato de testes

?

## Formulário PIP

?

```bash
pip install pytest
```

## Modelo para estimativa de tamanho

?
C

## Folha de cálculos do PROBE

![PROBE Report](https://user-images.githubusercontent.com/37521313/189774757-5b62ec38-6a8e-41b5-9841-1ec668f26e8c.png)

## Registro de tempo

![Registro de tempo](https://user-images.githubusercontent.com/37521313/189775387-b4470123-467e-43c3-91de-d6f8c76c2e18.png)

## Registro de erros

- ERRO 1
  - Tipo: Function
  - Injetado: Code
  - Removido: After Development
  - Tempo: 5,7
  - Contador: 1
  - Descrição: rxy e r2 estão incorretos. Era um erro de precedência que cometi, copiei a fórmula errado.
  - Data: 08/09/2022
- ERRO 2
  - Tipo: Environment
  - Injetado: Test
  - Removido: After development
  - Tempo: 5
  - Contador: 1
  - Descrição: estava tentando passar dados por parametro no pytest, o q n pode ser feito.
  - Data: 12/09/2022

## Listagem do código fonte do programa

```python
# regressaoLinear.py
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
```

```python
# test.py
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
```

## Resultado dos testes

![resultado teste](https://user-images.githubusercontent.com/37521313/189774603-45034af5-4f11-42de-8a2f-64e3544df759.png)
