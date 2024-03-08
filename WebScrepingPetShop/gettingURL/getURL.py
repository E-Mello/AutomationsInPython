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


def extract_product_urls(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    product_list = soup.find('ul', class_='products-grid')
    urls = []

    if product_list:
        product_items = product_list.find_all('li', class_='item')

        for product_item in product_items:
            product_link = product_item.find(
                'a', class_='product-image')['href']
            urls.append(product_link)

    return urls


def main():
    url = "https://www.zebupetcenter.com.br/cachorros.html?cat=10&limit=all"
    page_source = get_page_source(url)
    product_urls = extract_product_urls(page_source)

    # Salve as URLs em um arquivo de texto
    with open('product_urls.txt', 'w', encoding='utf-8') as file:
        for url in product_urls:
            file.write(f'{url}\n')


if __name__ == "__main__":
    main()
