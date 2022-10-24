# Relatório PSP2.1

**Autor:** Alexandre Aparecido Scrocaro Junior \
**email:** alescrocaro@gmail.com

**Professor:** Marco Aurélio Graciotto Silva\
**Universidade Tecnológica Federal do Paraná (UTFPR)**

## Formulário de Resumo de Planejamento de Projeto
### Relatório do planejamento de código e lógica
![image](https://user-images.githubusercontent.com/37521313/197648190-bb8d4c0f-c590-4fbc-9b65-9683d2dc329f.png)


### Resumo do planejamento de tempo
![image](https://user-images.githubusercontent.com/37521313/197647745-d5276d04-6b9a-4530-8a35-62f071758935.png)


### Resumo do planejamento de tamanho
![image](https://user-images.githubusercontent.com/37521313/197647801-8cc18fdb-8fb6-4422-b8e8-0326fe4f996b.png)


![image](https://user-images.githubusercontent.com/37521313/197647936-470ee19b-9267-4c49-8ddf-bff8cedef803.png)



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
![image](https://user-images.githubusercontent.com/37521313/197647801-8cc18fdb-8fb6-4422-b8e8-0326fe4f996b.png)


![image](https://user-images.githubusercontent.com/37521313/197647936-470ee19b-9267-4c49-8ddf-bff8cedef803.png)



## Folha de cálculos do PROBE
![image](https://user-images.githubusercontent.com/37521313/197650485-8be2d662-32a6-4b4c-83f9-7fbee3d35093.png)

![image](https://user-images.githubusercontent.com/37521313/197650518-0c1d7051-3618-4fdd-b706-4753827d5112.png)



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
![image](https://user-images.githubusercontent.com/37521313/197651879-dfc78834-2284-444b-a432-56b714e149e2.png)



## Registro de erros
![image](https://user-images.githubusercontent.com/37521313/197651914-1d8c8ec6-1887-4fe7-b5a0-03e912479859.png)


![image](https://user-images.githubusercontent.com/37521313/197651925-d3e95f8c-479d-4667-b41b-692d88edc965.png)



## Listagem do código fonte do programa



## Resultados dos testes


