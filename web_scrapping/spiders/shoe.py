# -*- coding: utf-8 -*-
import json
import time

import scrapy
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from random import randint

class ShoeSpider(scrapy.Spider):
    name = 'shoe_spider'
    allowed_domains = ['www.shop.travisscott.com']

    start_urls = [
        'https://shop.travisscott.com/']

    custom_settings = {
        'RETRY_ENABLED': False
    }

    headless_browser = False

    def __init__(self):
        self.driver = self.initialize_web_driver()

    def initialize_web_driver(self):
        # Add additional Options to the webdriver
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--kiosk")
        # add the argument and make the browser Headless.
        if self.headless_browser:
            chrome_options.add_argument("--headless")
        # Instantiate the Webdriver: Mention the executable path of the webdriver you have downloaded
        # if driver is in PATH, no need to provide executable_path
        driver = webdriver.Chrome(executable_path='E:/chromedriver_win32/chromedriver.exe', options=chrome_options)
        print('got driver')
        return driver

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse_wu, errback=self.failure, dont_filter=True)

    def parse_wu(self, response):
        print('url: {}'.format(response.url))

        try:
            self.driver.get(response.url)
            self.driver.implicitly_wait(5)
            while True:
                try:
                    sleep(5)
                    print('refreshing page')
                    self.driver.refresh()
                except:
                    pass

            print('completed')

        except Exception as ex:
            print('exception block')
            print(ex)
        finally:
            print('finally')
            # self.driver.close()

        self.driver.quit()

    def failure(self, failure):
        # log all failures
        self.logger.error(repr(failure))
        item = {}
        item['Web Address'] = failure.request.url
        print('item: {}'.format(item))
        yield None
