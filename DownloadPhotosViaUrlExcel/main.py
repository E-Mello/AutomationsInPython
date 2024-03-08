import pandas as pd
import requests
import os
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse
import time
import re


def download_and_save_image(id_produto, descricao, url_imagem, index):
    try:
        # Fazer requisição HTTP e obter conteúdo da imagem
        response = requests.get(url_imagem, timeout=10)
        response.raise_for_status()

        # Criar pasta para salvar a imagem, se necessário
        pasta = "pg_01"
        os.makedirs(pasta, exist_ok=True)

        # Salvar a imagem no disco
        with open(f"{pasta}/{id_produto}-{clean_filename(descricao)}-{index}.jpg", "wb") as f:
            f.write(response.content)

        # Aguardar um curto período de tempo para garantir que a imagem seja salva antes de prosseguir
        time.sleep(0.5)

    except requests.exceptions.Timeout:
        # Caso de timeout, tentar novamente após 2 segundos
        print(f"Timeout ao baixar imagem, tentando novamente: {url_imagem}")
        time.sleep(2)
        download_and_save_image(id_produto, descricao, url_imagem, index)

    except Exception as e:
        print(f"Erro ao baixar imagem: {url_imagem}")
        print(e)


def clean_filename(filename):
    # Remove caracteres especiais e substitui espaços por underscores
    filename = re.sub(r'[^\w\s.-]', '', filename)
    filename = re.sub(r'\s', '_', filename)
    return filename


# Ler o arquivo CSV
df = pd.read_csv("rel_produto_pag_1.csv", skiprows=1, delimiter=';')

# Cria a pasta "imagens" se não existir
os.makedirs("pg_01", exist_ok=True)

# Usar ThreadPoolExecutor para paralelizar os downloads
with ThreadPoolExecutor() as executor:
    # Iterar pelas linhas do DataFrame
    for i in range(df.shape[0]):
        # Obter ID e descrição do produto
        id_produto = df.iloc[i, 0]
        descricao = df.iloc[i, 1]

        # Iterar pelas colunas 2 a 6
        for j in range(2, 6):
            # Verificar se a coluna existe e tem uma URL de imagem
            if not pd.isnull(df.iloc[i, j]):
                url_imagem = df.iloc[i, j]

                # Obter o índice da imagem
                index = j - 1

                # Executar o download e salvamento em paralelo
                executor.submit(download_and_save_image,
                                id_produto, descricao, url_imagem, index)
