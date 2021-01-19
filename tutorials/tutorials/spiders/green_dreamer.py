import scrapy
from scrapy.selector import Selector

class PostSpider(scrapy.Spider):
    name = "ngo_posts"
    start_urls = [
        'https://greendreamer.com/journal/environmental-organizations-nonprofits-for-a-sustainable-future'
        # w tym przypakdu mamy tylko jedną stronę
    ]

    def parse(self, response):
        divs = response.css('div.sqs-block-content')
        for div in divs:
            for h in div.css("h3"):
                NGOname = h.xpath("./text()").extract()  # nazwa organizacji
                NGOdescrpit = h.xpath('following-sibling::p[1]/text()').extract()  # opis organizacji
                p = h.xpath('following-sibling::p[1]')
                NGOgetinvolved = h.xpath("following-sibling::p[strong[contains(.//text(), 'Get involved')]]").extract_first()

                if p.css('a') != []: #  nie chcemy fragmentu 'side note:'
                    NGOlink = p.css('a').attrib['href']  # adres organizacji
                    if NGOdescrpit:  # bez stopki
                        yield {
                            'Name': NGOname,
                            'Description': NGOdescrpit,
                            'Address': NGOlink,
                            'GetInvolved': NGOgetinvolved
                        }



