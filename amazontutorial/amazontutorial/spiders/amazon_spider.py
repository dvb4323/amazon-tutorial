import scrapy
from ..items import AmazontutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = "amazon_spider"
    start_urls = [
        "https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011%2Cp_n_feature_browse-bin%3A2656020011&dc&ds=v1%3AomzUY1t4dShIjr%2Fg9H%2BMbxhE8k9x4AogGHxH4iCF5G4&qid=1720972620&rnid=618072011&ref=sr_nr_p_n_feature_browse-bin_2"
    ]

    def parse(self, response):
        items = AmazontutorialItem()

        product_name = response.css('.a-color-base.a-text-normal::text').extract()
        product_author = response.css('.a-color-secondary .a-row .a-size-base+ .a-size-base').css('::text').extract()
        product_price = response.css('.puis-price-instructions-style .a-price-fraction , .puis-price-instructions-style .a-price-whole').css('::text').extract()
        product_image_link = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_image_link'] = product_image_link

        yield items
