# Scrapy para Raspagem de Anúncios de Carros Fiat

Este projeto Scrapy tem como objetivo extrair informações de anúncios de carros da marca Fiat de um site específico. Ele foi configurado para facilitar a coleta de dados como modelo, ano e preço, permitindo uma análise posterior dos anúncios disponíveis.

## Estrutura do Projeto

O projeto está estruturado da seguinte forma:


car_scraping/
├── scrapy.cfg         # Arquivo de configuração do Scrapy
├── .gitignore         # Lista de arquivos e pastas ignorados pelo Git
├── README.md          # Este arquivo, contendo informações sobre o projeto
└── car_scraping/       # Módulo principal do projeto
├── init.py
├── items.py         # Definição dos itens (modelos de dados) a serem raspados
├── middlewares.py   # Middlewares do Scrapy (processamento das requisições e respostas)
├── pipelines.py     # Pipelines para processar os itens raspados
├── settings.py      # Configurações do projeto Scrapy
└── spiders/         # Diretório contendo os spiders
├── init.py
└── cars_fiat.py # Spider específico para raspar os anúncios de carros Fiat


## Configuração

Antes de executar o spider, verifique e ajuste as seguintes configurações no arquivo `car_scraping/car_scraping/settings.py`:

- `BOT_NAME`: Nome do bot (pode ser mantido como `car_scraping`).
- `SPIDER_MODULES` e `NEWSPIDER_MODULE`: Devem apontar para o diretório de spiders do projeto.
- `ROBOTSTXT_OBEY`: Se deve ou não respeitar o arquivo `robots.txt` do site (recomendado manter como `True`).
- `DOWNLOAD_DELAY`: Delay entre as requisições para evitar sobrecarregar o servidor do site (ajuste conforme necessário).

Além disso, é crucial ajustar as seguintes configurações no arquivo do spider (`car_scraping/car_scraping/spiders/cars_fiat.py`):

- `allowed_domains`: Domínio do site a ser raspado.
- `start_urls`: URL inicial da página de listagem de carros.
- `parse()`: Método que contém a lógica para extrair os dados dos anúncios. **Ajuste os seletores CSS** para corresponder à estrutura HTML do site.

## Execução

Para executar o spider, navegue até o diretório raiz do projeto (`car_scraping/`) e execute o seguinte comando no terminal:

```bash
scrapy crawl cars_fiat
