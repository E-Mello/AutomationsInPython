import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup

SubCategoriesCachorro = {
    "Rações": "https://www.zebupetcenter.com.br/cachorros.html?cat=10&limit=all",
    "Higiene e Limpeza": "https://www.zebupetcenter.com.br/cachorros.html?cat=11&limit=all",
    "Medicina e Saúde": "https://www.zebupetcenter.com.br/cachorros.html?cat=12&limit=all",
    "Acessórios para Alimentação": "https://www.zebupetcenter.com.br/cachorros.html?cat=13&limit=all",
    "Adestramento e Comportamento": "https://www.zebupetcenter.com.br/cachorros.html?cat=14&limit=all",
    "Brinquedos": "https://www.zebupetcenter.com.br/cachorros.html?cat=15&limit=all",
    "Caixas e Bolsas de Transporte": "https://www.zebupetcenter.com.br/cachorros.html?cat=16&limit=all",
    "Caminhas e Outros": "https://www.zebupetcenter.com.br/cachorros.html?cat=17&limit=all",
    "Casinhas e acessórios": "https://www.zebupetcenter.com.br/cachorros.html?cat=18&limit=all",
    "Colerias, Guias e Peitorais": "https://www.zebupetcenter.com.br/cachorros.html?cat=19&limit=all",
    "Ossinhos e Petiscos": "https://www.zebupetcenter.com.br/cachorros.html?cat=21&limit=all",
    "Roupas e Acessórios": "https://www.zebupetcenter.com.br/cachorros.html?cat=22&limit=all",
    "Shampoos e Cosméticos": "https://www.zebupetcenter.com.br/cachorros.html?cat=23&limit=all",
}

SubCategoriesGato = {
    "Rações": "https://www.zebupetcenter.com.br/gatos.html?cat=24&limit=all",
    "Caixa de Areia e Limpeza": "https://www.zebupetcenter.com.br/gatos.html?cat=25&limit=all",
    "Medicina e Saúde": "https://www.zebupetcenter.com.br/gatos.html?cat=26&limit=all",
    "Acessórios para Alimentação": "https://www.zebupetcenter.com.br/gatos.html?cat=27&limit=all",
    "Adestramento e Comportamento": "https://www.zebupetcenter.com.br/gatos.html?cat=28&limit=all",
    "Brinquedos": "https://www.zebupetcenter.com.br/gatos.html?cat=29&limit=all",
    "Caixa e Bolsas de Transportes": "https://www.zebupetcenter.com.br/gatos.html?cat=30&limit=all",
    "Caminhas e Arranhadores": "https://www.zebupetcenter.com.br/gatos.html?cat=31&limit=all",
    "Coleiras e Acessórios": "https://www.zebupetcenter.com.br/gatos.html?cat=32&limit=all",
    "Higiene e Limpeza": "https://www.zebupetcenter.com.br/gatos.html?cat=33&limit=all",
    "Petiscos": "https://www.zebupetcenter.com.br/gatos.html?cat=34&limit=all"

}

SubCategoriesRoedor = {
    "Ração e Alimentos": "https://www.zebupetcenter.com.br/outros-pets/roedores/rac-o-e-alimentos.html?limit=all",
    "Gaiolas e Acessórios": "https://www.zebupetcenter.com.br/outros-pets/roedores/gaiolas-e-acessorios.html?limit=all",
    "Acessórios para Alimentação": "https://www.zebupetcenter.com.br/outros-pets/roedores/acessorios-para-alimentac-o.html?limit=all",
    "Higiene e Limpeza": "https://www.zebupetcenter.com.br/outros-pets/roedores/higiene-e-limpeza.html?limit=all",
    "Ninhos e Camas": "https://www.zebupetcenter.com.br/outros-pets/roedores/ninhos-e-camas.html?limit=all",
    "Medicina e Saúde": "https://www.zebupetcenter.com.br/outros-pets/roedores/medicina-e-saude.html?limit=all",
    "Pó para Banho": "https://www.zebupetcenter.com.br/outros-pets/roedores/po-para-banho.html?limit=all",
    "Acessórios para Roedores": "https://www.zebupetcenter.com.br/outros-pets/roedores/acessorios-para-roedores.html?limit=all"

}

SubCategoriesPassaro = {
    "Gaiolas e Acessórios": "https://www.zebupetcenter.com.br/outros-pets/passaros/gaiolas-e-acessorios.html?limit=all",
    "Alimentação": "https://www.zebupetcenter.com.br/outros-pets/passaros/alimentac-o.html?limit=all",
    "Medicina e Saúde": "https://www.zebupetcenter.com.br/outros-pets/passaros/medicina-e-saude.html?limit=all",
    "Acessórios para Alimentação": "https://www.zebupetcenter.com.br/outros-pets/passaros/acessorios-para-alimentac-o.html?limit=all",
    "Limpeza para Gaiolas": "https://www.zebupetcenter.com.br/outros-pets/passaros/limpeza-para-gaiolas.html?limit=all"
}

SubCategoriesReptil = {
    "Ração, Vitaminas e Outros": "https://www.zebupetcenter.com.br/outros-pets/repteis/rac-o-vitaminas-e-outros.html?limit=all",
    "Acessórios para Alimentação": "https://www.zebupetcenter.com.br/outros-pets/repteis/acessorios-para-alimentac-o.html?limit=all",
    "Habitat e Acessórios": "https://www.zebupetcenter.com.br/outros-pets/repteis/habitat-e-acessorios.html?limit=all",
    "Luzes e Aquecedores": "https://www.zebupetcenter.com.br/outros-pets/repteis/luzes-e-aquecedores.html?limit=all"
}

subcategories = {
    "Cachorro": SubCategoriesCachorro,
    "Gato": SubCategoriesGato,
    "Roedores": SubCategoriesRoedor,
    "Passaros": SubCategoriesPassaro,
    "Repteis": SubCategoriesReptil
}

# Crie o driver do Chrome
driver = webdriver.Chrome()


def create_folders(category, subcategory):
    category_folder = category.replace(" ", "_")
    subcategory_folder = subcategory.replace(" ", "_")
    os.makedirs(os.path.join(category_folder,
                subcategory_folder), exist_ok=True)


def get_page_source(url):
    driver.get(url)  # Navega até o URL especificado
    driver.implicitly_wait(10)
    page_source = driver.page_source
    return page_source


def extract_subcategory_links(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    links = []
    dd_element = soup.find('dd', class_='odd')
    a_elements = dd_element.find_all('a')
    for a_element in a_elements:
        href = a_element['href']
        links.append(href)
    return links


def download_images(images, product_folder):
    for i, image_url in enumerate(images):
        image_path = os.path.join(product_folder, f"image_{i}.jpg")
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(image_path, 'wb') as file:
                file.write(response.content)


def access_and_extract_product_info(subcategory_links, category):
    for link in subcategory_links:
        driver.get(link)  # Navega até o link da subcategoria
        select_element = driver.find_element(
            By.CSS_SELECTOR, 'select[title="Resultados por página"]')
        select_element.find_element(
            By.CSS_SELECTOR, 'option[value*="limit=all"]').click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.invisibility_of_element_located(
            (By.CSS_SELECTOR, 'div.loading-mask')))
        products_div = driver.find_element(
            By.CSS_SELECTOR, 'div.category-products')
        product_li_elements = products_div.find_elements(
            By.CSS_SELECTOR, 'li.item')

        for product_li in product_li_elements:
            product_link_element = product_li.find_element(
                By.CSS_SELECTOR, 'a.product-image')
            product_link = product_link_element.get_attribute('href')
            product_name = product_li.find_element(
                By.CSS_SELECTOR, 'h2.product-name a').text
            try:
                product_description = product_li.find_element(
                    By.CSS_SELECTOR, 'div.short-description').text
            except NoSuchElementException:
                product_description = "Descrição não encontrada"

            # Navegue até a página do produto
            driver.get(product_link)

            # Aqui você pode obter as informações adicionais do produto e imagens
            product_page_source = driver.page_source
            # Extraia informações adicionais, como preço, etc. da product_page_source

            # Extraia e baixe imagens
            product_img_elements = product_li.find_elements(
                By.CSS_SELECTOR, 'div.product-image-gallery img')
            product_images = [img.get_attribute(
                'src') for img in product_img_elements]

            # Crie as pastas para categoria e subcategoria
            create_folders(category, product_name)

            # Crie uma pasta para o produto
            product_folder = os.path.join(category.replace(
                " ", "_"), product_name.replace(" ", "_"))
            os.makedirs(product_folder, exist_ok=True)

            # Salve as informações do produto em um arquivo .txt
            info_file = os.path.join(product_folder, "info.txt")
            with open(info_file, "w", encoding="utf-8") as file:
                file.write(f"Nome: {product_name}\n")
                file.write(f"Descrição: {product_description}\n")

            # Download de imagens
            download_images(product_images, product_folder)


def main():
    for category, subcategory_links in subcategories.items():
        for subcategory, url in subcategory_links.items():
            page_source = get_page_source(url)
            subcategory_links = extract_subcategory_links(page_source)
            access_and_extract_product_info(subcategory_links, category)


if __name__ == "__main__":
    main()
