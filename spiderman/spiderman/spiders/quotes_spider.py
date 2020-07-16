import scrapy
from ..items import SpidermanItem
from scrapy.http import Request, FormRequest
from scrapy.utils.response import open_in_browser


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'http://quotes.toscrape.com/login'
    ]
    
    def parse(self, response):
        token = response.css("form input::attr(value)").extract_first()
        print("Token: ", token)
        return FormRequest.from_response(
            response,
            formdata={
                "csrf_token" : token,
                "username" : "bangbang",
                "password" : "asdf"
            },
            callback=self.start_scraping
        )
    
    def start_scraping(self, response):
        open_in_browser(response)
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

        if next_page is not None:
            url = 'http://quotes.toscrape.com' + next_page
            yield Request(url, self.start_scraping)
