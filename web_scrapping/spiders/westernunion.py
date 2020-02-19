# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class WesternUnionSpider(scrapy.Spider):
    name = 'western_union'
    allowed_domains = ['www.westernunion.com']
    start_urls = ['https://www.westernunion.com/us/en/web/send-money/start/']

    custom_settings = {
        'RETRY_ENABLED': False
    }

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='E:/chromedriver_win32/chromedriver.exe')
        print('got driver')

    def start_requests(self):
        for url in self.start_urls:
            # yield scrapy.Request(url, callback=self.parse_exchange_rate, errback=self.failure, dont_filter=True)
            yield scrapy.Request(url, callback=self.parse_country_list, errback=self.failure, dont_filter=True)

    def parse_exchange_rate(self, response):
        print('url: {}'.format(self.start_urls))
        self.driver.get(response.url)
        _selector = self.driver.find_element_by_xpath('//*[@id="smoExchangeRate"]')
        print('Exchange Rate:\n{}'.format(_selector.text))
        return None

    def parse_country_list(self, response):
        print('url: {}'.format(self.start_urls))
        self.driver.implicitly_wait(30)
        self.driver.get(response.url)

        # select the dropdown button once it is availble
        #dropdown = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="smonewuser"]/div/app-sendmoney-option/div[2]/div[1]/div/div/form/app-country-dropdown/div/ul')))

        #WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='smonewuser']/div/app-sendmoney-option//span[text()='United States]"))).click()



        # search all options
        # options = self.driver.find_elements_by_css_selector(".hy-country-container .hy-country")
        # print all option text
        for elem in self.driver.find_elements_by_xpath('.//span[@class = "hy-country"]'):
            print(elem.text)

        # _selector = self.driver.find_element_by_class_name('dropdown-menu')
        # print('Country List:\n{}'.format(options))
        return None

    def failure(self, failure):
        # log all failures
        self.logger.error(repr(failure))
        item = {}
        item['Web Address'] = failure.request.url
        print('item: {}'.format(item))
        yield None
