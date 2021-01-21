import scrapy

class RecipeSpider(scrapy.Spider):
    name = "recipes"
    start_urls = [
        'https://www.przepisy.pl/przepis/aromatyczna-zupa-krem-z-batatow-z-curry'
    ]

    def parse(self, response):
        ingredients = response.css('div.ingredients-list-content-item')
        for ingredient in ingredients:
            ingredient_name = ingredient.css('::text').get()
            ingredient_quantity = ingredient.css('.quantity span::text').get()
            yield {
                'ingredient_name': ingredient_name,
                'ingredient_quantity': ingredient_quantity
            }
        dish_size = response.css('div.person-count::text').get()
        #print(dish_size)
        dish_name = response.css('title::text').get()
        #print(dish_name)
        steps = response.css('div.step-info')
        for step in steps:
            print(step.css('p::text').get())




