<div align="center">
  <h1>🌍 Google and Bing Maps Data Collection 🗺️</h1>
  <p>
    <img src="https://img.shields.io/github/repo-size/E-Mello/GoogleAndBingMapsDataCollection" alt="GitHub repo size">
    <img src="https://img.shields.io/github/stars/E-Mello/GoogleAndBingMapsDataCollection" alt="GitHub stars">
    <img src="https://img.shields.io/github/forks/E-Mello/GoogleAndBingMapsDataCollection" alt="GitHub forks">
    <img src="https://img.shields.io/github/license/E-Mello/GoogleAndBingMapsDataCollection" alt="GitHub license">
  </p>
</div>

## Descrição do Projeto

Este projeto é uma automação para coletar dados de locais no Google Maps e no Bing Maps usando Python. Ele permite pesquisar diferentes categorias de locais em uma cidade específica nos dois serviços e salvar os resultados em arquivos CSV. O projeto inclui os seguintes componentes:

- **collectDataBingWebScraping.py**: Realiza web scraping no Bing Maps para coletar dados de locais e salvar em um arquivo CSV.

- **collectDataGoogleAPI.py**: Utiliza a API do Google Maps para pesquisar e coletar dados de locais em uma cidade específica. Os resultados são salvos em um arquivo CSV.

- **fixEncode.py**: Script para corrigir problemas de codificação de caracteres nos dados coletados, se necessário.

- **insertDataOtherSiteWebScraping.py**: Automatiza o processo de inserção dos dados coletados em outro site usando web scraping.

## Commits

O projeto foi desenvolvido em várias etapas. Os commits foram feitos de forma organizada e descritiva para facilitar o acompanhamento do progresso.

## Pré-requisitos

- Python 3.x
- **Bibliotecas Python:** [requirements.txt](https://github.com/E-Mello/GoogleAndBingMapsDataCollection/blob/main/requirements.txt)
- **Chave de API do Google Maps** (para `collectDataGoogleAPI.py`)
- **Conta de e-mail e senha** (para `collectDataBingWebScraping.py` e `insertDataOtherSiteWebScraping.py`)

## Instruções de Uso

1. Clone o repositório para sua máquina local.
2. Instale as bibliotecas Python necessárias executando `pip install -r requirements.txt`.
3. Configure as chaves de API e as credenciais necessárias nos arquivos apropriados.
4. Execute os scripts de acordo com suas necessidades para coletar e manipular os dados de locais.

## Autor

- **Édio de Melo Pereira**

## Licença

Este projeto está disponível sob a licença MIT, o que significa que é gratuito e pode ser usado, modificado e distribuído por qualquer pessoa.

---
