import googlemaps
import csv

# Defina sua chave da API do Google aqui
API_KEY = 'SUA_API_KEY'

# Nome do arquivo CSV para salvar os resultados
nome_arquivo_csv = 'resultado.csv'

# Categorias de interesse (você pode adicionar mais categorias conforme necessário)
categorias = ['restaurant', 'hotel', 'public_transport',
              'bank', 'supermarket', 'store', 'hospital', 'cool things to do', 'tourist attractions']

# Crie um conjunto para armazenar lugares únicos
lugares_unicos = set()

# Crie um cliente da API# Nome do arquivo CSV para salvar os resultados
nome_arquivo_csv = 'resultado_blumenau.csv'

# Categorias de interesse (você pode adicionar mais categorias conforme necessário)
categorias = ['restaurant', 'hotel', 'public_transport',
              'bank', 'supermarket', 'store', 'hospital', 'cool things to do', 'tourist attractions']

# Crie um conjunto para armazenar lugares únicos
lugares_unicos = set()

# Crie um cliente da API do Google Maps
gmaps = googlemaps.Client(key=API_KEY)

# Define os limites de latitude e longitude para Blumenau, SC (ajuste conforme necessário)
lat_min = -26.9583
lat_max = -26.7883
lon_min = -49.1683
lon_max = -49.0483

# Define a resolução da grade em graus (ajuste conforme necessário)
resolucao_grade = 0.002  # Aproximadamente 200 metros

# Abra o arquivo CSV em modo de escrita
with open(nome_arquivo_csv, 'w', newline='', encoding='utf-8') as arquivo_csv:
    writer = csv.writer(arquivo_csv)

    # Escreva o cabeçalho do CSV
    writer.writerow(['Nome', 'Endereço', 'Latitude', 'Longitude', 'Categoria'])

    # Percorre a grade de coordenadas
    for lat in range(int(lat_min * 10000), int(lat_max * 10000), int(resolucao_grade * 10000)):
        for lon in range(int(lon_min * 10000), int(lon_max * 10000), int(resolucao_grade * 10000)):
            latitude = lat / 10000.0
            longitude = lon / 10000.0

            for categoria in categorias:
                # Use a API do Google Maps para buscar lugares próximos
                places = gmaps.places_nearby(
                    location=(latitude, longitude), radius=2000, keyword=categoria)

                # Verifique se a solicitação foi bem-sucedida
                if 'results' in places:
                    # Itere pelos resultados e obtenha os detalhes de cada lugar
                    for place in places['results']:
                        nome = place['name']
                        endereco = place.get('vicinity', '')
                        latitude = place['geometry']['location']['lat']
                        longitude = place['geometry']['location']['lng']
                        # Verifique se este lugar já foi registrado para evitar repetições
                        if nome not in lugares_unicos:
                            lugares_unicos.add(nome)
                            writer.writerow(
                                [nome, endereco, latitude, longitude, categoria])
                            print(f'Nome: {nome}')
                            print(f'Endereço: {endereco}')
                            print(f'Latitude: {latitude}')
                            print(f'Longitude: {longitude}')
                            print(f'Categoria: {categoria}')
                            print('-' * 30)

print(f'Resultados salvos em {nome_arquivo_csv}')
