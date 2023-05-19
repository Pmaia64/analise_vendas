# Importar biblioteca os ( para percorrer pastas de arquivos - base de dados)
# Leitura de arquivos em uma pasta
# Utilização do for (executa a base de dados para cada arquivo)


import os
lista_arquivo = os.listdir("C:/Users/Paulo Maia/Desktop/Projeto 4 Consolidação Vendas/Vendas")
print(lista_arquivo)
for arquivo in lista_arquivo:
    print(arquivo)


