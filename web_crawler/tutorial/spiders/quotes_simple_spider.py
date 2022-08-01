from scrapy import Spider, Request


class QuotesSpider(Spider):
    name = 'quotes-simple'
    start_urls = [f'https://quotes.toscrape.com/page/{page}/' for page in range(1, 11)]

    # If 'start_urls' is defined like above, then this method is not needed.
    # It is here anyway to show what happens to the URLs under the hood.
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

    # Handle the response for each URL
    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = f'quotes-{page}.html'

        # Save the response in a HTML file
        with open(filename, 'wb') as f:
            f.write(response.body)

        self.log(f'Saved file {filename}')
