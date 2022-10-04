import json
import numpy
import statistics

with open('dados.json', encoding='utf-8') as dados_json:
    dados = json.load(dados_json)



def calcula_loc_per_method(dados):
    for i in range(len(dados)):
        if 'method_amount' in dados[0]:
            dados[i]['loc_per_method'] = dados[i]['size'] / dados[i]['method_amount']
        else:
            dados[i]['loc_per_method'] = dados[i]['size']

    return dados
#end-function

def calcula_somatoria_ln(dados):   
    somatoria = 0
    for i in range(len(dados)):
        somatoria = somatoria + numpy.log(dados[i]['loc_per_method'])

    return somatoria
#end-function

def calcula_media(dados, somatoria):
    return somatoria / len(dados)
#end-function


def calcula_variancia(dados, media):
    somatoria = 0
    for i in range(len(dados)):
        somatoria = somatoria + (numpy.log(dados[i]['loc_per_method']) - media)**2

    return somatoria/(len(dados)-1)
#end-function

def calcula_dp(variancia):
    return variancia**(1/2)
#end-function

def calcula_faixas(media, dp):
    return [media-2*dp, media-dp, media, media+dp, media+2*dp]
#end-function

def calcula_valores_limite(faixas):
    e = 2.718
    return [e**faixas[0], e**faixas[1], e**faixas[2], e**faixas[3], e**faixas[4]]
#end-function


################ TESTES ################ 

dados_tamanho_definido = calcula_loc_per_method(dados['table1'])
somatoria = calcula_somatoria_ln(dados_tamanho_definido)
media = calcula_media(dados_tamanho_definido, somatoria)
variancia = calcula_variancia(dados_tamanho_definido, media)
dp = calcula_dp(variancia)
faixas = calcula_faixas(media, dp)
valores = calcula_valores_limite(faixas)

print(media, variancia, dp)
print(faixas)
print(valores)