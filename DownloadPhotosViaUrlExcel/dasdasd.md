# Etapas:

Importar bibliotecas:

pandas: para leitura do arquivo CSV.
requests: para realizar requisições HTTP e baixar as imagens.
os: para criar pastas e salvar os arquivos.
Ler o arquivo CSV:

Usar o pandas para ler o arquivo CSV e armazená-lo em um DataFrame.
Pular a primeira linha (cabeçalho) com df.skiprows(1).
Iterar pelas linhas do DataFrame:

Para cada linha, verificar se há URL de imagem nas colunas 3 a 8.
Se houver URL, baixar a imagem e salvá-la com o nome formatado: ID-Descrição.jpg.
Usar a biblioteca requests para realizar a requisição HTTP e obter o conteúdo da imagem.
Usar a biblioteca os para criar a pasta para salvar a imagem, se necessário.
Salvar a imagem no disco com o nome formatado.
Tratar erros:

Implementar tratamento de erros para lidar com URLs inválidas ou falhas no download da imagem.
