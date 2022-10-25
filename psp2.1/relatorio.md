# Relatório PSP2.1

**Autor:** Alexandre Aparecido Scrocaro Junior \
**email:** alescrocaro@gmail.com

**Professor:** Marco Aurélio Graciotto Silva\
**Universidade Tecnológica Federal do Paraná (UTFPR)**

## Formulário de Resumo de Planejamento de Projeto
### Relatório do planejamento de código e lógica
![image](https://user-images.githubusercontent.com/37521313/197648190-bb8d4c0f-c590-4fbc-9b65-9683d2dc329f.png)

### Resumo de planejamento de projeto
![image](https://user-images.githubusercontent.com/37521313/197647745-d5276d04-6b9a-4530-8a35-62f071758935.png)

### Resumo do planejamento de tempo
![image](https://user-images.githubusercontent.com/37521313/197652564-6765bfd0-c635-4163-86f9-cb5dbd4537b0.png)

### Resumo do planejamento de tamanho
![image](https://user-images.githubusercontent.com/37521313/197652236-929e3cd4-c5bb-42d0-bbae-3d13ebc4c98a.png)


![image](https://user-images.githubusercontent.com/37521313/197652290-a2872060-02e8-4bee-ac78-7c0f8518422f.png)



## Modelo de relato de testes
Realizei testes para cada uma das linhas da Tabela 1 do [documento de requisitos do programa 6](https://github.com/magsilva/psp-training/blob/master/Activity-PSP2.1/ASGKIT%20PROG6.pdf). Utilizei a ferramenta [Pytest](https://docs.pytest.org/) para me auxiliar, alcançando uma cobertura de 96%.\
O comando utilizado foi:

```bash
pytest -v --cov=main test.py 
```

E os testes realizados foram os abaixo (também encontrados no arquivo test.py)\
![image](https://user-images.githubusercontent.com/37521313/197649315-3f255f15-57db-4d49-b95c-641102b70d70.png)



## Lista de verificação de projeto



## Lista de verificação de código



## Formulário PIP

### Descrição do problema
Encontrei problemas ao ler o [documento de requisitos do programa](https://github.com/magsilva/psp-training/blob/master/Activity-PSP2.1/ASGKIT%20PROG6.pdf), que, ao meu ver, foi pouco explícito nas explicações, vide a explicação da função que deveria ser integrada. Além disso, eu segui os passos da busca especificada e não cheguei a um código que encontrasse o x para os valores de teste dados na Tabela 1 do documento, acredito que esse problema foi inserido por algum erro que cometi, mas não o encontrei.

### Descrição de proposta
A única proposta seria explicitar mais acerca da função a ser utilizada.



## Modelo para estimativa de tamanho
![image](https://user-images.githubusercontent.com/37521313/197652676-ab5fe0cd-48b6-4c39-a0cb-276bd9269ff4.png)

![image](https://user-images.githubusercontent.com/37521313/197652720-f730f2c7-9c0e-4bba-85cf-2c07dbbe2590.png)



## Folha de cálculos do PROBE
![image](https://user-images.githubusercontent.com/37521313/197652783-ca7ced91-09b1-4fd8-a778-8c40d7a0b19a.png)

![image](https://user-images.githubusercontent.com/37521313/197652811-71606a75-7584-4908-a04b-afb9043e06e9.png)



## Especificação de histórias e casos de uso
- Calculo da integral: já realizado no programa 5;
- Ajustar valor de x: utilizar resultado obtido da integração e comparar com o resultado esperado (p);
- Ajustar valor de d: utilizar erro obtido na integração e comparar sinal com sinal do erro tolerável.



## Documentação das interfaces do projeto

### verifica_resultado(esperado, obtido, e)
Compara o resultado obtido na integração e o resultado que se era esperado e retorna a flag 'alto' || 'baixo' || 'aceitavel', que será utilizada para ajustar o valor de x.

### ajustar_x(x, d, flag_diferenca)
Compara a flag_diferença com 'alto' ou com 'baixo' e ajusta o valor de x, utilizando d.

### ajustar_d(erro, d)
Verifica se o sinal do erro obtido na integração é negativo e ajusta o d conforme a comparação. 

### busca_x(dof, p)
Realiza a busca do valor de x, seguindo os passos presentes no [documento de requisitos do programa 6](https://github.com/magsilva/psp-training/blob/master/Activity-PSP2.1/ASGKIT%20PROG6.pdf)


## Registro de tempo
![image](https://user-images.githubusercontent.com/37521313/197652045-1255c50c-3a74-4ae4-b8bf-f529d2ee194e.png)



## Registro de erros
### Defeito 1
#### Inserido
Code
#### Removido
Code
#### Descrição
eu havia esquecido de mudar a chamada da função integral, pois mudei sua declaração inserindo a variavel dof

### Defeito 2
#### Inserido
Planning
#### Removido
Code
#### Descrição
Programei toda a logica e o resultado não foi o esperado, então comecei a procurar pelo bug.
com 16 minutos encontrei o bug: o d não está mudando nunca.
com 18 minutos, encontrei a causa do bug, erro no planejamento: estava comparando variaveis erradas; ao invés de comparar o sinal do erro da integracao com o erro aceitavel, comparei o sinal do erro aceitavel com o sinal da integracao.
nao cheguei a uma solucao entao vou perguntar ao professor.
descobri o que estava acontecendo mas nao consegui resolver, entao encontrei uma forma de contornar o bug.

### Resumo
![image](https://user-images.githubusercontent.com/37521313/197651914-1d8c8ec6-1887-4fe7-b5a0-03e912479859.png)


![image](https://user-images.githubusercontent.com/37521313/197651925-d3e95f8c-479d-4667-b41b-692d88edc965.png)



## Listagem do código fonte do programa
```python
from simpson import *

def verifica_resultado(esperado, obtido, e):
  if (not esperado): return None
  if (not obtido): return None
  if (not e): return None
  
  diferenca =  esperado - obtido
  
  if diferenca == 0: 
    return 'aceitavel'

  elif diferenca > 0: # esperado > obtido
    if diferenca > e:
      return 'baixo' # deve realizar passo 3 ou 6

    return 'aceitavel' # chegou no resultado esperado ou proximo dele

  elif diferenca < 0: # esperado < obtido
    diferenca = diferenca * -1

    if diferenca > e:
      return 'alto' # deve realizar passo 4 ou 7

    return 'aceitavel' # chegou no resultado esperado ou proximo dele
#end-function

def ajustar_x(x, d, flag_diferenca):
  if (x < 0): return None
  if (d == 0): return x
  if (d < 0): return None
  if (not flag_diferenca): return None

  if flag_diferenca == 'baixo': # resultado eh muito baixo
    return x + d

  elif flag_diferenca == 'alto': # resultado eh muito baixo
    return x - d
#end-function

def ajustar_d(erro, d):
  if (not erro): return None
  if (not d): return None

  if erro >= 0:
    return d

  return d/2
#end-function

def busca_x(dof, p):
  if (not dof): return None

  e = 0.00001
  x = 1
  d = 0.5
  i = 0

  result, erro = simpson(x, e, dof)
  flag_diferenca = verifica_resultado(p, result, e)
  if flag_diferenca == 'aceitavel': 
    return x
  x = ajustar_x(x, d, flag_diferenca)

  while True:
    result, erro = simpson(x, e, dof)

    flag_diferenca = verifica_resultado(p, result, e)
    if flag_diferenca == 'aceitavel': 
      return x
    d = ajustar_d(erro, d)
    x = ajustar_x(x, d, flag_diferenca)

    # sleep(0.2)
    i = i+1
    if(d <= 0): return x
    if(i > 100000): return None
#end-function

```


## Resultados dos testes
![image](https://user-images.githubusercontent.com/37521313/197653042-3bdcfd30-a04a-4b99-bebf-7764ebdf47a7.png)


