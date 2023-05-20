# Importar biblioteca os ( para percorrer pastas de arquivos - base de dados)
# Leitura de arquivos em uma pasta
# Utilização do for (executa a base de dados para cada arquivo)


import os
import pandas as pd
lista_arquivo = os.listdir("C:/Users/Paulo Maia/Desktop/Projeto 4 Consolidação Vendas/Vendas")

tabela_total = pd.DataFrame()
#Importar as bases de dados de vendas
for arquivo in lista_arquivo:
    if "Vendas" in arquivo:
        
        #importar o arquivo
        tabela = pd.read_csv(f"C:/Users/Paulo Maia/Desktop/Projeto 4 Consolidação Vendas/Vendas/{arquivo}")
        tabela_total = tabela_total.append(tabela)
        
print(tabela_total)
