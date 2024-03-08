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

    return product_name, product_description, product_image


def main():
    # URL da página de categorias
    categories_url = "https://www.zebupetcenter.com.br/cachorros.html?cat=10&limit=all"
    page_source = get_page_source(categories_url)
    soup = BeautifulSoup(page_source, 'html.parser')

    # Encontre todos os links para produtos na página de categorias
    product_links = [a['href']
                     for a in soup.find_all('a', class_='product-image')]

    # Crie o diretório com o nome da categoria (no caso, 'Cachorros')
    category_directory = 'Cachorros'
    if not os.path.exists(category_directory):
        os.makedirs(category_directory)

    # Itere pelas URLs dos produtos
    for index, row in enumerate(product_links):
        product_url = row
        page_source = get_page_source(product_url)
        product_name, product_description, product_image_url = extract_product_info(
            page_source)

        # Crie o diretório com o nome do produto (limpo) dentro da categoria
        product_directory = os.path.join(
            category_directory, clean_filename(product_name))
        if not os.path.exists(product_directory):
            os.makedirs(product_directory)

        # Salve os dados do produto em um arquivo de texto
        with open(f'{product_directory}/{clean_filename(product_name)}.txt', 'w', encoding='utf-8') as file:
            file.write(f'Nome: {product_name}\n')
            file.write(f'Descrição: {product_description}\n')

        # Faça o download da imagem do produto
        image_data = requests.get(product_image_url).content
        with open(f'{product_directory}/{clean_filename(product_name)}.jpg', 'wb') as image_file:
            image_file.write(image_data)


if __name__ == "__main__":
    main()
