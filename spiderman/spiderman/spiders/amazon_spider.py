import scrapy
from ..items import AmazonSpidermanItem

class AmazonSpider(scrapy.Spider):
    name = "amazon"
    start_urls = [
        "https://www.amazon.com/Books-Last-30-days/s?rh=n%3A283155%2Cp_n_publication_date%3A1250226011"
    ]

    def parse(self, response):
        data = AmazonSpidermanItem()

        book_name = response.css(".a-color-base.a-text-normal").css('::text').extract()
        book_author = response.css(".sg-col-12-of-28 .a-size-base+ .a-size-base").css('::text').extract()
        price = response.css(".a-spacing-top-small .a-price-whole").css('::text').extract()       
        fraction = response.css(".a-price-fraction").css('::text').extract()       
        book_image_url = response.css(".s-image::attr(src)").extract()
        
        book_price = price+'.'+fraction

        data['book_name'] = book_name
        data['book_author'] = book_author
        data['book_price'] = book_price
        data['book_image_url'] = book_image_url
        yield data
    

        