from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
import time

# Defina a cidade e a lista de categorias
cidade = "Guabiruba"
categorias = ["Restaurantes", "Hoteis", "Supermercados", "Comércios", "Escolas",
              "Hospitais", "Clinicas", "Farmácias", "Postos de gasolina", "Coisas para fazer", "Bares"]

# Conjunto para lugares únicos
lugares_unicos = set()


def pesquisar_categorias(driver):
    for categoria in categorias:
        # Navegue para a página de pesquisa do Google Maps
        driver.get("https://www.google.com/maps")

        # Encontre o campo de pesquisa e insira a categoria desejada
        search_box = driver.find_element(By.ID, "searchboxinput")
        pesquisa = f"{categoria} em {cidade}"
        search_box.send_keys(pesquisa)
        search_box.send_keys(Keys.RETURN)

        # Esperar por alguns segundos para os resultados carregarem
        time.sleep(5)

        # Função para coletar informações dos resultados
        coletar_resultados(driver, categoria)


def coletar_resultados(driver, categoria):
    # Esperar que os resultados carreguem completamente
    time.sleep(5)

    # Encontre os resultados no mapa
    resultados = driver.find_elements_by_css_selector(".section-result")

    for resultado in resultados:
        try:
            # Clique no resultado para abrir mais informações
            resultado.click()
            time.sleep(3)  # Aguarde um momento para carregar as informações

            # Encontre as informações do lugar
            nome = driver.find_element_by_css_selector(
                ".section-hero-header-title-title").text
            endereco = driver.find_element_by_css_selector(
                ".section-info-text").text

            # Obtenha a URL atual, que contém as coordenadas da latitude e longitude
            url = driver.current_url
            latitude, longitude = extrair_latitude_longitude(url)

            # Verificar se este lugar já foi adicionado aos lugares únicos
            if (nome, endereco, latitude, longitude) not in lugares_unicos:
                lugares_unicos.add((nome, endereco, latitude, longitude))

        except Exception as e:
            print(f"Erro ao coletar informações: {str(e)}")
            continue  # Continue com a próxima iteração

    # Chamar a função para salvar os dados em um arquivo CSV com base no nome da cidade e categoria
    salvar_csv(list(lugares_unicos), cidade, categoria)


def extrair_latitude_longitude(url):
    # A URL contém as coordenadas de latitude e longitude
    partes_url = url.split("/")
    # Remova o último elemento (zoom)
    coordenadas = partes_url[-1].split(",")[:-1]
    latitude = coordenadas[0]
    longitude = coordenadas[1]
    return latitude, longitude


def salvar_csv(dados, nome_cidade, categoria):
    nome_arquivo = f"googleMaps_{nome_cidade}_{categoria}.csv"
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
        writer = csv.writer(arquivo_csv)

        # Escrever o cabeçalho do CSV
        writer.writerow(["Nome", "Endereço", "Latitude", "Longitude"])

        # Escrever os dados dos resultados
        writer.writerows(dados)


def main():
    driver = webdriver.Chrome()

    # Função para pesquisar as categorias
    pesquisar_categorias(driver)

    # Fechar o navegador no final
    driver.quit()


if __name__ == "__main__":
    main()
