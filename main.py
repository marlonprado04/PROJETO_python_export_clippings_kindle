"""
Passos:
1. Acessar o arquivo
2. Separar o arquivo em blocos
3. Tratar blocos de texto para ficarem todos em 3 linha
4. Adicionar array com blocos de texto de 3 linhas
5. Criar CSV com cada uma das 3 linhas dos blocos

"""
import pandas as pd

# PASSO 1: ACESSA ARQUIVO

# Abre o arquivo .txt em modo de leitura
with open('./files/test_clippings.txt', 'r', encoding='utf-8') as file:
    # Lê o conteúdo do arquivo
    content = file.read()

# PASSO 2: SEPARA ARQUIVO EM BLOCO
# PASSO 3: TRATAR BLOCOS EM 3 LINHAS
# PASSO 4: ADICIONAR BLOCOS EM UM ARRAY DE 3 LINHAS

# Separa os blocos de conteúdo pelos marcadores "=========="
blocks = content.split('==========')


# Cria lista vazia para os blocos
list_of_blocks = []

# Itera sobre cada bloco
for index, block in enumerate(blocks):
    # Remove linhas em volta do bloco atual
    block = block.strip()

    # Inicializa uma lista vazia para cada bloco
    list_of_blocks.append([])

    # Itera cada linha do bloco atual
    for line in block.splitlines():
        # Verifica se linha não é vazia
        if line.strip():
            # Adiciona linha no índice bloco atual do array
            list_of_blocks[index].append(line)
    
# PASSO 5: PASSAR O ARRAY PARA UM CSV / DATAFRAME

# Cria um DataFrame a partir da lista de dicionários
df = pd.DataFrame(list_of_blocks)

# Salva o DataFrame em um arquivo CSV
df.to_csv('output.csv', index=False)