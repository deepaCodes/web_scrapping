# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait


class ProductspiderSpider(scrapy.Spider):
    name = 'ProductSpider'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com/dp/B003CHUWQA/']
    _base_url = 'https://www.amazon.com'

    headless = False

    def __init__(self):
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path='E:/chromedriver_win32/chromedriver.exe',
                                       chrome_options=chrome_options)
        print('got driver')

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse_product, errback=self.failure, dont_filter=True)

    def parse_product(self, response):
        print('parsing website')
        try:
            self.driver.get(response.url)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//span[@id="unqualified-buybox-olp"]')))

            price = self.driver.find_element_by_xpath('//*[@id="unqualified-buybox-olp"]/div/span').text
            print('price: {}'.format(price))
        except Exception as ex:
            print(ex)
        finally:
            self.driver.quit()


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
            # _url = '{}{}'.format(self._base_url, price_url)
            _url = 'https://www.amazon.com/gp/offer-listing/B003CHUWQA/ref=dp_olp_afts?ie=UTF8&condition=new'
            print('following link: {}'.format(_url))
            price = yield scrapy.Request(_url, callback=self.parse_price)
            # requests.get()

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

    def failure(self, failure):
        # log all failures
        print(repr(failure))
        yield None

    def parse_price(self, response):
        print('parse_price')
        return 1
