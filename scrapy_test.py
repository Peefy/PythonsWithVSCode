# python3 scrapy_test.py
# python scrapy_test.py
# python3 -m pip install scrapy
# python -m pip install scrapy

import scrapy

## scrapy runspider scrapy_test.py -o blog.json

class BlogSpider(scrapy.Spider):
    """
    this is a class test scrapy
    """
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        for title in response.css('h2.entry-title'):
            yield {'title': title.css('a ::text').extract_first()}

        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)

print('')
# python3 scrapy_test.py
# python scrapy_test.py
