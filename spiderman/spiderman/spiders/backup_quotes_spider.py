import scrapy
from ..items import SpidermanItem
from scrapy.http import Request


class QuotesSpider(scrapy.Spider):
    name = "backup_quotes"

    start_urls = [
        'http://quotes.toscrape.com/'
    ]
    
    def parse(self, response):
        items = response.css("div.quote")
        data = SpidermanItem()

        for item in items:
             
            title = item.css("span.text::text").extract_first()
            author = item.css(".author::text").extract_first()
            tag = item.css(".tag::text").extract()
            data["title"] = title
            data["author"] = author
            data["tag"] = tag
            yield data

        # next_page = response.xpath("//li[@class='next'] //a[href]").get()
        next_page = response.css("li.next a::attr(href)").get()
        print(next_page)
        if next_page is not None:
            url = 'http://quotes.toscrape.com' + next_page
            yield Request(url, self.parse)