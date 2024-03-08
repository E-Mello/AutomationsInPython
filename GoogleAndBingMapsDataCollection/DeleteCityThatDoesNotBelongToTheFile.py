import csv
import os

# Defina a cidade que você deseja procurar
cidade_desejada = 'Balneário Camboriú'

# Nome do arquivo CSV
arquivo = "resultado_itajai.csv"

# Nome do arquivo de saída temporário
arquivo_temporario = "temporario.csv"

# Abra o arquivo CSV
with open(arquivo, mode="r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # Lê o cabeçalho

    # Índices das colunas que você deseja manter
    colunas_desejadas = [0, 1, 2, 3]

    # Crie um arquivo de saída temporário
    with open(arquivo_temporario, mode="w", encoding="utf-8", newline="") as csv_output_file:
        csv_writer = csv.writer(csv_output_file)
        # Escreva o cabeçalho apenas com as colunas desejadas
        csv_writer.writerow([header[i] for i in colunas_desejadas])

        # Verifique cada linha do arquivo CSV original
        for row in csv_reader:
            # A segunda coluna (índice 1) contém a informação de endereço
            endereco = row[1]

            # Verifica se a cidade desejada não está presente no endereço
            if f", {cidade_desejada}" not in endereco:
                # Escreva a linha no arquivo de saída temporário
                linha_temporaria = [row[i] for i in colunas_desejadas]
                csv_writer.writerow(linha_temporaria)

# Substitua o arquivo original pelo arquivo temporário
os.replace(arquivo_temporario, arquivo)

print(
    f"As linhas correspondentes à cidade {cidade_desejada} foram removidas de {arquivo}.")
