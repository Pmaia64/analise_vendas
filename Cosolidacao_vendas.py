# Importar biblioteca os ( para percorrer pastas de arquivos - base de dados)
# Leitura de arquivos em uma pasta
# Utilização do for (importar a base de dados)


import os
lista_arquivo = os.listdir('C:/Users/Paulo Maia/Desktop/Projeto 4 Consolidação Vendas/Vendas_Lojas')
print(lista_arquivo)
for arquivo in lista_arquivo:
    print(arquivo)
    
