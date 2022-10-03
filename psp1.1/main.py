import json

with open('dados.json', encoding='utf-8') as dados_json:
    dados = json.load(dados_json)
#end-function

def calcula_media(dados):

    print(dados['table1'][0])
#end-function

calcula_media(dados)