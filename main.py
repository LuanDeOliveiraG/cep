from fastapi import FastAPI
from fastapi.params import Body
import pandas as pd
import os
import asyncio as asinc

dados = pd.read_csv(os.path.join(os.getcwd(),'API_CEP','api','bq-CEPs.csv'), sep=",", encoding="utf-8")

app= FastAPI()

@app.get("/uf/{sigla_uf}")
async def busca_geral_uf(sigla_uf:str):
    """Retorna os todos os CEPs em Json de uma determinada UF (sempre em maiusculo na requisição)."""
    return dados[dados['sigla_uf'] == sigla_uf.upper()].to_json(index=False, orient="records") #para nao ir com index

@app.get('/{numero}')
async def busca_cep(numero:int):
    """Retorna os seguintes campos: 'cep', 'logradouro', 'localidade', 'id_municipio', 'nome_municipio','sigla_uf'."""
    validacao = str(numero)
    if len(validacao) < 8:
        return {"Erro": "insira um CEP Válido (mais de 7 caracteres)"}
    return dados[dados["cep"] == numero].to_json(index=False, orient="records")

@app.get('/municipio/{id_municipio}')
async def busca_id_municipio(id_municipio:int):
    """Retorna os seguintes campos: 'cep', 'logradouro', 'localidade', 'id_municipio', 'nome_municipio','sigla_uf'. Com base no municipio."""
    validacao = str(id_municipio)
    if len(validacao)<5:
        return {"Erro": "insira um id_municipio valido, ou revise o enviado!"}
    else:
        return dados[dados["id_municipio"] == validacao].to_json(index=False, orient="records")















# @app.put('/inserir')
# async def atualiza_dados(cep:int = Body(...),
#                          logradouro:str = Body(...), 
#                          localidade:str = Body(...), 
#                          id_municipio:int = Body(...), 
#                          nome_municipio:str = Body(...), 
#                          sigla_uf:str = Body(...)):
#     "Atualiza e insere dados novos no registro"
#     try:
#         atualizacao = {
#             'cep':cep ,
#             'logradouro': logradouro,
#             'localidade': localidade,
#             'id_municipio': id_municipio,
#             'nome_municipio': nome_municipio,
#             'sigla_uf': sigla_uf
#         }
#         dadonovo = pd.DataFrame(atualizacao, index=[0])
#         dados = pd.concat([dados,dadonovo])
#         print(dadonovo)

#         return {'Atualizado':f"Registro: {atualizacao}"}
#     except Exception as erro:
#         return {"erro":f"descrição do erro: {erro}\n {atualizacao}"}

    
