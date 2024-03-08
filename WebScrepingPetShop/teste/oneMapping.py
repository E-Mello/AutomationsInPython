import os
from selenium import webdriver
from bs4 import BeautifulSoup

# Função para limpar caracteres inválidos para nomes de arquivos


def clean_filename(filename):
    # Substitui caracteres inválidos por sublinhados (_)
    return "".join(x if x.isalnum() or x in {'_', ' ', '.'} else '_' for x in filename)


# Crie o driver do Chrome
driver = webdriver.Chrome()


def get_page_source(url):
    driver.get(url)
    driver.implicitly_wait(10)
    page_source = driver.page_source
    return page_source


def extract_product_info(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    product_list = soup.find('ul', class_='products-grid')

    if product_list:
        product_items = product_list.find_all('li', class_='item')

        for product_item in product_items:
            product_name = product_item.find(
                'h2', class_='product-name').text.strip()
            product_price = product_item.find(
                'span', class_='price').text.strip()

            # Verifica se o elemento com a classe 'availability' existe
            availability_element = product_item.find(
                'p', class_='availability')
            if availability_element:
                product_availability = availability_element.text.strip()
            else:
                product_availability = "Não disponível"

            # Limpa o nome do produto para uso como nome de arquivo
            cleaned_product_name = clean_filename(product_name)

            # Crie o diretório 'teste' se ele não existir
            if not os.path.exists('teste'):
                os.makedirs('teste')

            # Crie um arquivo de texto para cada item dentro do diretório 'teste'
            with open(f'teste/{cleaned_product_name}.txt', 'w', encoding='utf-8') as file:
                file.write(f'Nome: {product_name}\n')
                file.write(f'Preço: {product_price}\n')
                file.write(f'Disponibilidade: {product_availability}\n')


def main():
    url = "https://www.zebupetcenter.com.br/cachorros.html?cat=10&limit=all"
    page_source = get_page_source(url)
    extract_product_info(page_source)


if __name__ == "__main__":
    main()
