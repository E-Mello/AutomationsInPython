import csv

# Defina a cidade que você deseja procurar
cidade_desejada = "Balneário Camboriú"

# Nome do arquivo CSV de entrada e saída
arquivo_entrada = "resultado_itajai.csv"
arquivo_saida = "balneario_camboriu.csv"

# Crie um conjunto temporário para armazenar as linhas correspondentes à cidade
linhas_temporarias = []

# Abra o arquivo CSV de entrada
with open(arquivo_entrada, mode="r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # Lê o cabeçalho

    # Índices das colunas que você deseja manter
    colunas_desejadas = [0, 1, 2, 3]

    # Verifique cada linha do arquivo CSV
    for row in csv_reader:
        # A terceira coluna (índice 2) contém a informação de endereço
        endereco = row[1]

        # Verifica se a cidade desejada está presente no endereço
        if f", {cidade_desejada}" in endereco:
            # Crie uma nova linha apenas com as colunas desejadas
            linha_temporaria = [row[i] for i in colunas_desejadas]
            linhas_temporarias.append(linha_temporaria)

# Se houver linhas correspondentes à cidade, crie um novo arquivo CSV
if linhas_temporarias:
    with open(arquivo_saida, mode="w", encoding="utf-8", newline="") as csv_output_file:
        csv_writer = csv.writer(csv_output_file)
        # Escreva o cabeçalho apenas com as colunas desejadas
        csv_writer.writerow([header[i] for i in colunas_desejadas])

        # Escreva as linhas correspondentes à cidade
        csv_writer.writerows(linhas_temporarias)

print(
    f"As linhas correspondentes à cidade {cidade_desejada} foram salvas em {arquivo_saida}.")
