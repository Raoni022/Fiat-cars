import scrapy

class CarsSpider(scrapy.Spider):
    name = 'cars_fiat'  # Nome do spider alterado para identificar a finalidade
    allowed_domains = ['example.com']  # Mantenha ou ajuste para o domínio real
    start_urls = ['https://example.com/cars']  # URL inicial

    def parse(self, response):
        # Itera sobre cada anúncio de carro
        for car in response.css('div.car-Listing'):  # Ajuste o seletor conforme necessário
            make = car.css('span.car-make::text').get()  # Extrai a marca
            model = car.css('span.car-model::text').get()  # Extrai o modelo
            year = car.css('span.car-year::text').get()    # Extrai o ano
            price = car.css('span.car-price::text').get()  # Extrai o preço

            # Verifica se a marca é Fiat (insensível a maiúsculas/minúsculas)
            if make and make.lower() == 'fiat':
                yield {
                    'make': make,
                    'model': model,
                    'year': year,
                    'price': price,
                }

        # Segue links de paginação se houver
        for href in response.css('a.next-page::attr(href)'):  # Ajuste o seletor
            yield response.follow(href, self.parse)       
BOT_NAME = 'car_scraping'

SPIDER_MODULES = ['car_scraping.spiders']
NEWSPIDER_MODULE = 'car_scraping.spiders'


# Configurações de respeito aos robots.txt e atrasos
ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 1

