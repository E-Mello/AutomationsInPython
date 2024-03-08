import os
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re

# Função para limpar caracteres inválidos para nomes de arquivos


def clean_filename(filename):
    # Remove todos os caracteres inválidos e substitui espaços por sublinhados
    return re.sub(r'[\/:*?"<>|]', '', filename).replace(' ', '_')


# Crie o driver do Chrome
driver = webdriver.Chrome()


def get_page_source(url):
    driver.get(url)
    driver.implicitly_wait(10)
    page_source = driver.page_source
    return page_source


def extract_product_info(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    product_name = soup.find(
        'div', class_='product-name').find('h1').text.strip()
    product_description = soup.find(
        'div', class_='short-description').find('div', class_='std').text.strip()
    product_image = soup.find('img', id='image-main')['src']
    product_price_element = soup.find('span', class_='price')
    if product_price_element:
        product_price = product_price_element.text.strip()
    else:
        product_price = "N/A"  # Ou algum valor padrão se o preço não for encontrado
    return product_name, product_description, product_image, product_price


def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def main():
    # URL da página de categorias
    categories_url = "https://www.zebupetcenter.com.br/gatos.html?cat=24&limit=all"
    page_source = get_page_source(categories_url)
    soup = BeautifulSoup(page_source, 'html.parser')

    # Links para produtos na página de categorias
    product_links = [a['href']
                     for a in soup.find_all('a', class_='product-image')]

    # Categoria principal
    main_category = 'Gatos'

    # Iterar pelas URLs dos produtos
    for index, row in enumerate(product_links):
        product_url = row
        page_source = get_page_source(product_url)
        product_name, product_description, product_image_url = extract_product_info(
            page_source)

        # Diretório com o nome da categoria principal (por exemplo, 'Cachorros')
        create_directory(main_category)

        sub_category = 'Rações'

        # Diretório com o nome da subcategoria dentro da categoria principal
        sub_category_directory = os.path.join(main_category, sub_category)
        create_directory(sub_category_directory)

        # Diretório com o nome do produto (limpo) dentro da subcategoria
        product_directory = os.path.join(
            sub_category_directory, clean_filename(product_name))
        create_directory(product_directory)

        # Salvar os dados do produto em um arquivo de texto
        with open(f'{product_directory}/{clean_filename(product_name)}.txt', 'w', encoding='utf-8') as file:
            file.write(f'Nome: {product_name}\n')
            file.write(f'Descrição: {product_description}\n')
            file.write(f'Preço: {product_price}\n')

        # Download da imagem do produto
        image_data = requests.get(product_image_url).content
        with open(f'{product_directory}/{clean_filename(product_name)}.jpg', 'wb') as image_file:
            image_file.write(image_data)


if __name__ == "__main__":
    main()
