import scrapy

class RecipeSpider(scrapy.Spider):
    name = "recipes"
    start_urls = [
        'https://www.przepisy.pl/przepis/aromatyczna-zupa-krem-z-batatow-z-curry'
    ]

    def parse(self, response):
        dish_size = response.css('div.person-count::text').get()
        print(dish_size)
        dish_name = response.css('title::text').get()
        print(dish_name)
        ingredients = response.css('div.ingredients-list-content-item')
        for ingredient in ingredients:
            ingredient_name = ingredient.css('::text').get()
            ingredient_quantity = ingredient.css('.quantity span::text').get()
            yield {
                'ingredient_name': ingredient_name,
                'ingredient_quantity': ingredient_quantity
            }
        steps = response.css('div.step-info')
        for step in steps:
            print(step.css('p::text').get())
        # first recommended recipe
        next_url = response.css('div.recommended-wrapper')
        next_url_href = next_url.css('a ::attr(href)').get()
        if next_url_href is not None:  # jesli strona istnieje
            next_url_href = response.urljoin(next_url_href)  # zamienia relatywne linki na absolutne
            print(next_url_href)
            #yield scrapy.Request(next_url_href, callback=self.parse)  # znowu wywolujemy to samo tylko na innej stronie





