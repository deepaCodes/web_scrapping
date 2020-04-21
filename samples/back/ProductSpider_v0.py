# -*- coding: utf-8 -*-
import requests
import scrapy


class ProductspiderSpider(scrapy.Spider):
    name = 'ProductSpider'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com/dp/B003CHUWQA/']
    _base_url = 'https://www.amazon.com'

    def parse(self, response):
        # print('parsing website')

        request_url = response.meta['redirect_urls'][-1]
        asin = [url for url in str(request_url).split('/') if url][-1]
        product_name = response.xpath('//span[@id="productTitle"]/text()').get()
        # price = response.xpath('//*[@id="unqualified-buybox-olp"]/div/span').get()

        image_url = response.xpath('//img[@id="landingImage"]/@src').get()
        alt_images = [img for img in
                      response.xpath('//div[@id="altImages"]//span[@class="a-button-text"]/img/@src').getall() if
                      str(img).endswith('.jpg')]

        ingredients = [info.xpath('.//p/text()').get() for info in
                       response.xpath('//*[@id="important-information"]/div[2]') if
                       info.xpath('.//span[@class="a-text-bold"]/text()').get() == 'Ingredients']

        price_url = response.xpath('//div[@id="availability"]/span/a/@href').get()
        if price_url:
            #_url = '{}{}'.format(self._base_url, price_url)
            _url = 'https://www.amazon.com/gp/offer-listing/B003CHUWQA/ref=dp_olp_afts?ie=UTF8&condition=new'
            print('following link: {}'.format(_url))
            price = yield scrapy.Request(_url, callback=self.parse_price)
            #requests.get()

        product = {
            'ASIN': asin,
            'Link': request_url,
            'Product Name': str(product_name).strip(),
            'Price': price,
            'Ingredients': ingredients.pop(0) if len(ingredients) > 0 else None,
            'Picture (URL)': image_url,
            'Picture of nutritrion information': '\n'.join(alt_images),

        }
        print(product)

        yield product

    def parse_price(self, response):
        print('parse_price')
        return 1
