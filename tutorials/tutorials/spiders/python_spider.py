import scrapy


class PostSpider(scrapy.Spider):
    name = "posts"
    start_urls = [
        'https://blog.scrapinghub.com/'  # przejscie przez wszystkie strony
    ]

    def parse(self, response):
        for post in response.css('div.post-item'):
            yield {
                'title': post.css('.post-header h2 a::text')[0].get(),
                'date': post.css('.post-header a::text')[1].get(),
                'author': post.css('.post-header a::text')[2].get()
            }
        next_page = response.css('a.next-posts-link::attr(href)').get() #  przejscie 'dalej' element a o klasie next post link wyciagnieta wartosc atrybutu href
        print(dir(next_page))
        if next_page is not None:
            next_page = response.urljoin(next_page)  #  zamienia relatywne linki na absolutne
            yield scrapy.Request(next_page, callback=self.parse)  #  yield (przypomniec sobie!!!)  callback=self.parse kolejne wywolanie parse
