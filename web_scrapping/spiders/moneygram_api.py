# -*- coding: utf-8 -*-
import re
from threading import Thread

import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from bs4 import BeautifulSoup


class MoneygramSpider(scrapy.Spider):
    name = 'moneygram'
    allowed_domains = ['www.moneygram.com']
    start_urls = [
        'https://www.moneygram.com/mgo/us/en/']

    custom_settings = {
        'RETRY_ENABLED': False
    }

    headless = True

    def __init__(self):
        print('Init done')

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse_exchange_rate, errback=self.failure, dont_filter=True)

    def parse_exchange_rate(self, response):
        print('url: {}'.format(self.start_urls))
        soup = BeautifulSoup(response.text, "lxml")
        # print(soup)
        pattern = re.compile(r"window.__env.clientKey =*?;")
        script = soup.find("script", text=pattern)
        print(script)
        match = re.search(r'window.__env.clientKey =(.*?);', soup.text).group(1)
        print(match)
        exchange_rate = None
        print('Receiving country: India, exchange rate: {}'.format(exchange_rate))
        print('done')
        return None

    def failure(self, failure):
        # log all failures
        self.logger.error(repr(failure))
        item = {}
        item['Web Address'] = failure.request.url
        print('item: {}'.format(item))
        yield None
