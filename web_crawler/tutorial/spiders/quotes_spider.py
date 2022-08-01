from scrapy import Spider


class QuotesSpider(Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/page/1/']

    # Handle the response for each URL
    def parse(self, response):
        # Extract the data from each quote on the page
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        # If there are links to the next page, follow them
        yield from response.follow_all(css='li.next a', callback=self.parse)      
