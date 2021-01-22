import scrapy


class PostSpider(scrapy.Spider):  # klasa dziedzicząca po scrapy.Spider (nasza wersja)
    name = "posts" #  nazwa crawlera po ktorym identyfikujemy, któy wywołać
    start_urls = [
        'https://blog.scrapinghub.com/'  # początkowy link (lub lista linkow do przeszukania)
    ]

    def parse(self, response):  # response - zwracane dane
        for post in response.css('div.post-item'):
            yield {
                'title': post.css('.post-header h2 a::text')[0].get(),
                'date': post.css('.post-header a::text')[1].get(),
                'author': post.css('.post-header a::text')[2].get()
            }
        next_page = response.css('a.next-posts-link::attr(href)').get() #  przejscie 'dalej' element a o klasie next post link wyciagnieta wartosc atrybutu href
        if next_page is not None: #  jesli strona istnieje
            next_page = response.urljoin(next_page)  #  zamienia relatywne linki na absolutne
            yield scrapy.Request(next_page, callback=self.parse) #  znowu wywolujemy to samo tylko na innej stronie