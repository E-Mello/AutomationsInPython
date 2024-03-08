import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Defina a cidade e a lista de categorias
cidade = "Indaial"
categorias = ["Restaurantes", "Lanches", "Padarias", "Oficinas", "Pontos turisticos", "Prefeitura", "Posto de Sáude",
              "Lojas", "Roupa", "Moto", "Carro", "Dentista", "Hoteis", "Supermercados", "Comércio", "Escolas",
              "Colégios", "Bicicleta", "Construção", "Saúde", "Comida", "Passeios", "Idosos", "Parques", "Praças",
              "Monumentos",  "Hospitais", "Clinicas", "Farmácias", "Postos de gasolina", "Coisas para fazer", "Bares",
              "Cinemas", "Teatros", "Museus", "Bibliotecas", "Estádios", "Ginásios", "Zoológicos", "Jardins Botânicos",
              "Estações de Trem", "Aeroportos", "Bancos", "Correios", "Hotéis", "Piscinas", "Esportes", "Universidades",
              "Faculdades", "Escolas de Idiomas", "Igrejas", "Mesquitas", "Sinagogas", "Templos", "Lojas de Eletrônicos",
              "Lojas de Roupas", "Lojas de Calçados", "Lojas de Livros", "Lojas de Brinquedos", "Lojas de Bebidas",
              "Lojas de Móveis", "Lojas de Artigos para Casa", "Lojas de Beleza", "Salões de Beleza", "Barbearias", "Shopping",
              "Lojas de Decoração", "Lojas de Informática", "Lojas de Joias", "Joalherias", "Lojas de Esportes", "Academias", "Beach",
              "Lojas de Automóveis", "Concessionárias", "Lojas de Ferramentas", "Lojas de Jardinagem", "Floriculturas", "Praias", "Praia"]

# Conjunto para lugares únicos
lugares_unicos = set()

# Variável para o caminho do arquivo CSV para comparação
# Defina o caminho do arquivo ou deixe em branco ""
csv_para_comparar = ""


def pesquisar_categorias(driver):
    for categoria in categorias:
        # Navegar para a página de pesquisa do Bing Maps
        driver.get("https://www.bing.com/maps")

        # Encontrar o campo de pesquisa e inserir a categoria desejada
        search_box = driver.find_element(By.ID, "maps_sb")
        pesquisa = f"{categoria} em {cidade}"
        search_box.send_keys(pesquisa)
        search_box.send_keys(Keys.RETURN)

        # Esperar por alguns segundos para os resultados carregarem
        time.sleep(5)

        # Função para coletar informações dos resultados
        coletar_resultados(driver, categoria)


def verificar_dados_csv(nome, endereco):
    if csv_para_comparar == "":
        return True  # Ignorar a verificação se csv_para_comparar estiver vazio

    # Verifique apenas o nome no arquivo CSV
    try:
        with open(csv_para_comparar, mode="r", encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader)

            for row in csv_reader:
                if nome == row[0]:
                    return False  # O nome já está no arquivo CSV

    except FileNotFoundError:
        pass

    return True  # O nome não foi encontrado no arquivo CSV


def coletar_resultados(driver, categoria):
    # Encontrar a lista de pontos encontrados na barra lateral esquerda
    lista_pontos = driver.find_elements(
        By.CSS_SELECTOR, "ul.b_vList.b_divsec > li")

    for ponto in lista_pontos:
        try:
            # Extrair informações relevantes do ponto encontrado
            dados_ponto = ponto.find_element(
                By.CSS_SELECTOR, "a.listings-item").get_attribute("data-entity")

            nome = dados_ponto.split('"title":"')[1].split('"')[0]
            endereco = dados_ponto.split('"address":"')[1].split('"')[0]

            # Verificar se a cidade desejada está no endereço
            if cidade.lower() not in endereco.lower():
                continue  # Ignorar este resultado se a cidade não estiver no endereço

            # Latitude e longitude
            latitude = float(dados_ponto.split('"y":')[1].split(',')[0])
            longitude = float(dados_ponto.split('"x":')[1].split(',')[0])

            # Verificar se este lugar já foi adicionado aos lugares únicos e se não está no arquivo CSV
            if (nome, endereco, latitude, longitude) not in lugares_unicos and verificar_dados_csv(nome, endereco):
                lugares_unicos.add((nome, endereco, latitude, longitude))

        except NoSuchElementException:
            # Tratamento de erro caso o elemento não seja encontrado
            print(f"Elemento não encontrado para {categoria}")
            continue  # Continue com a próxima iteração

    # Chamar a função para salvar os dados em um arquivo CSV com base no nome da cidade
    salvar_csv(list(lugares_unicos), cidade)


def salvar_csv(dados, nome_cidade):
    nome_arquivo = f"resultados_{nome_cidade}.csv"
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
