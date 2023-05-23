# Importar biblioteca os ( para percorrer pastas de arquivos - base de dados)
# Leitura de arquivos em uma pasta
# Utilização do for (executa a base de dados para cada arquivo)

import os
import pandas as pd
import plotly.express as px


lista_arquivo = os.listdir("C:/Users/Paulo Maia/Desktop/Projeto 4 Consolidação Vendas/Vendas")

tabela_total = pd.DataFrame()
#Importar as bases de dados de vendas
for arquivo in lista_arquivo:
    if "Vendas" in arquivo:
        
        tabela = pd.read_csv(f"C:/Users/Paulo Maia/Desktop/Projeto 4 Consolidação Vendas/Vendas/{arquivo}")
        tabela_total = tabela_total.append(tabela)
print(tabela_total)
#Criação das tabelas pro agrupamento de dados
tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[['Quantidade Vendida', 'Preco Unitario']].sort_values(by='Quantidade Vendida', ascending=False)
print(tabela_produtos)
#Criação da tabela de faturamento total
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[['Faturamento']].sort_values(by='Faturamento', ascending=False)
print(tabela_faturamento)
#Criação da tabela por agrupamento de lojas
tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[['Faturamento']].sort_values(by='Faturamento', ascending=False)
print(tabela_lojas)
#Criação do gráfico para demonstrativo do raking de lojas
grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y='Faturamento')
grafico.show()
