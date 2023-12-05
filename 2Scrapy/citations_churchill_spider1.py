import scrapy

class ChurchillQuotesSpider(scrapy.Spider):
    name = "citations de Churchill"
    start_urls = ["http://evene.lefigaro.fr/citations/winston-churchill",]

    def parse(self, response):
        # Trouver l'auteur sur la page
        author = response.css('a[href="/celebre/biographie/winston-churchill-675.php"]::text').extract_first()

        for cit in response.xpath('//div[@class="figsco__quote__text"]'):
            text_value = cit.xpath('a//text()').extract_first()

            # Supprimer les caractères “ et ” avec la méthode replace
            cleaned_text = text_value.replace('“', '').replace('”', '')

            yield {'author': author, 'text': cleaned_text}