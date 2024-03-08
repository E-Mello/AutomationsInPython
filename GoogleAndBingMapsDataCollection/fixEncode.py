import csv
from unidecode import unidecode

# Função para corrigir caracteres em uma string


def corrigir_caracteres(texto):
    return unidecode(texto)


# Nome do arquivo CSV de entrada e saída
arquivo_csv_entrada = 'resultado_balneario_camboriu.csv'
arquivo_csv_saida = 'seuarquivo_corrigido.csv'

# Abre o arquivo de entrada e cria o arquivo de saída
with open(arquivo_csv_entrada, 'r', encoding='utf-8') as arquivo_entrada, open(arquivo_csv_saida, 'w', encoding='utf-8', newline='') as arquivo_saida:
    leitor_csv = csv.reader(arquivo_entrada)
    escritor_csv = csv.writer(arquivo_saida)

    # Processa o cabeçalho
    cabeçalho = next(leitor_csv)
    escritor_csv.writerow(cabeçalho)

    # Processa o restante das linhas
    for linha in leitor_csv:
        linha_corrigida = [corrigir_caracteres(campo) for campo in linha]
        escritor_csv.writerow(linha_corrigida)
