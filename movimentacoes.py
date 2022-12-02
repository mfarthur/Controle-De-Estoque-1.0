import pandas as pd
from pandas import *
import time
from random import randint
from openpyxl import *


arq1 = "estoque.xlsx"
arq2 = "historico.xlsx"
arq3 = "graficos.xlsx"

def cadastrarProduto(produto, descricao, preco, quantidade):

              df = pd.read_excel(arq1)
              identificação = f'{randint(1,9)}{randint(1,9)}{randint(1,9)}{randint(1,9)}'
              while identificação in df['ID']:
                     identificação = f'{randint(1,9)}{randint(1,9)}{randint(1,9)}{randint(1,9)}'
              dic = ({'ID': [identificação],
                     'Produto': [produto],
                     'Descrição': [descricao],
                     'Preço (R$)': [preco],
                     'Quantidade': [quantidade],
                     })
              dataframe = pd.DataFrame(dic)
              print(dataframe)
              dataframe = pd.concat([dataframe, df], ignore_index=True)
              dataframe.to_excel(arq1, index=False)

def removerProduto(id):
       #FUNÇÃO FUNCIONANDO, PORÉM NÃO ESTÁ SALVANDO
       try:
              df = pd.read_excel(arq1)
              linha = df.index[df['ID'] == id]
              df2 = df.drop(linha, axis=0)
              df2.to_excel(arq1, index=False)
       except:
              print("Linha digitada não existe")
       else:
              print("Produto Removido com sucesso")

def reduzirQuantidade(produto, id, quantidade):
       #FUNÇÃO FUNCIONANDO, PORÉM NÃO ESTÁ SALVANDO
       try:  
              df = pd.read_excel(arq1)
              linha = df.index[df['ID'] == id]
              produto = df.loc[linha, 'Produto']
              df.loc[linha, 'Quantidade'] += quantidade
              df.to_excel(arq1, index=False)
       except:
              print("Produto digitado não existe")
       else:
              try:
                     dataframe = pd.read_excel(arq2)
                     x = time.localtime()
                     data, hora = f"{x[2]}/{x[1]}/{x[0]}", f"{x[3]}:{x[4]}:{x[5]}"
                     alt = f'-{quantidade} unidades'
                     d = {'Data': [data],
                     'Horário': [hora],
                     'Produto': [produto],
                     'ID': [id],
                     'Alteração': [alt]
                     }
                     df = pd.DataFrame(d)
                     dataframe = pd.concat([dataframe, df], ignore_index=True)
                     df.to_excel(arq2, index=False)
              except:
                     print('Erro ao salvar histórico de alteração')
                     
def aumentarQuantidade(produto, id, quantidade):
       #FUNÇÃO FUNCIONANDO, PORÉM NÃO ESTÁ SALVANDO
       try:  
              df = pd.read_excel(arq1)
              linha = df.index[df['ID'] == id]
              produto = df.loc[linha, 'Produto']
              df.loc[linha, 'Quantidade'] -= quantidade
              df.to_excel(arq1, index=False)
       except:
              print("Produto digitado não existe")
       else:
              try:
                     dataframe = pd.read_excel(arq2)
                     x = time.localtime()
                     data, hora = f"{x[2]}/{x[1]}/{x[0]}", f"{x[3]}:{x[4]}:{x[5]}"
                     alt = f'+{quantidade} unidades'
                     d = {'Data': [data],
                     'Horário': [hora],
                     'Produto': [produto],
                     'ID': [id],
                     'Alteração': [alt]
                     }
                     df = pd.DataFrame(d)
                     dataframe = pd.concat([dataframe, df], ignore_index=True)
                     df.to_excel(arq2, index=False)
              except:
                     print('Erro ao salvar histórico de alteração')

def alterarPreco(produto,id, preço):
       #FUNÇÃO NÃO USADA POR AUSÊNCIA DE ABA, PORÉM MESMO ERRO DAS ANTERIORES
       try:  
              df = pd.read_excel(arq1)
              linha = df.index[df['ID'] == id]
              df.loc[linha, 'Valor Unitário'] = preço
              produto = df.loc[linha, 'Produto']
              df.to_excel(arq1, index=False)
       except:
              print("Produto digitado não existe")
       else:
              try:
                     dataframe = pd.read_excel(arq2)
                     x = time.localtime()
                     data, hora = f"{x[2]}/{x[1]}/{x[0]}", f"{x[3]}:{x[4]}:{x[5]}"
                     alt = f'Preço alterado para R$ {preço}'
                     d = {'Data': [data],
                     'Horário': [hora],
                     'Produto': [produto],
                     'ID': [id],
                     'Alteração': [alt]
                     }
                     df = pd.DataFrame(d)
                     dataframe = pd.concat([dataframe, df], ignore_index=True)
                     df.to_excel(arq2, index=False)
              except:
                     print('Erro ao salvar histórico de alteração')
