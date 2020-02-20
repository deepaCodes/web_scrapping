# -*- coding: utf-8 -*-
import time
from threading import Thread

import scrapy
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
import json
import random

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
        print('open file')
        with open('E:/python/web_scrapping/DATA/country.json', encoding='utf-8') as f:
            self.country_list = json.load(f)['countryList']

        print('countries: {}'.format(self.country_list))

        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path='E:/chromedriver_win32/chromedriver.exe',
                                       chrome_options=chrome_options)
        print('got driver')



    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse_exchange_rate, errback=self.failure, dont_filter=True)

    def parse_exchange_rate(self, response):
        print('url: {}'.format(self.start_urls))
        self.driver.get(response.url)

        try:  # proceed if element is found within 3 seconds otherwise will raise TimeoutException
            element = WebDriverWait(self.driver, 10). \
                until(EC.presence_of_element_located((By.XPATH, '//*[@id="receiveCountry"]')))
        except TimeoutException:
            print("Time out!")

        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="mat-dialog-0"]/mg-dialog/div/mat-icon').click()

        print('Exchange Rate Scrapping')

        exchange_rate_list = []
        for country in self.country_list:
            if not country['receiveOnline']:
                continue
            print(country)
            try:
                exchange_rate = self._get_exchange_rate(country)
                print('exchange_rate: {}'.format(exchange_rate))
                exchange_rate_list.append(country['name'] + ' '+ exchange_rate)
                time.sleep(random.randint(30, 60))
            except:
                print('error for :{}'.format(country))

        print('\n'.join(exchange_rate_list))
        return exchange_rate_list

    def _get_exchange_rate(self, country):
        # print response.body
        send = self.driver.find_element_by_xpath('//*[@id="send"]')
        send.clear()
        send.send_keys(1000)
        print('amount updated')
        time.sleep(1)
        receiveCountry = self.driver.find_element_by_xpath('//*[@id="receiveCountry"]')
        receiveCountry.clear()
        receiveCountry.send_keys(country['name'])
        print('country updated to: {}'.format(country['name']))
        time.sleep(1)
        receiveCountry.send_keys(Keys.RETURN)
        receiveCountry.send_keys(Keys.RETURN)
        try:
            exchange_rate_div = wait(self.driver, 5).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="mat-tab-content-0-0"]/div/mg-estimate-view/div/mg-exchange-rate/div')))
            exchange_rate = exchange_rate_div.text
        except:
            print('Timeout block')
            self.driver.find_element_by_xpath('//*[@id="mat-tab-content-0-0"]/div/mg-estimate-view/div/div[1]/div[2]/mg-change-receiver-location/div/a').click()
            time.sleep(2)
            return None

        baseReceiveCurrency = self.driver.find_element_by_xpath(
            '//*[@id="mat-tab-content-0-0"]/div/mg-estimate-view/div/div[1]/div[2]/mg-receive-amount/div/div/span[1]')
        print('baseReceiveCurrency: {}'.format(baseReceiveCurrency.text))

        print(exchange_rate)
        print('Receiving country: {}, exchange rate: {}'.format(country['name'], exchange_rate))
        time.sleep(1)
        print('go back to selection')
        self.driver.find_element_by_xpath('//*[@id="mat-tab-content-0-0"]/div/mg-estimate-view/div/div[1]/div[2]/mg-change-receiver-location/div/a').click()
        #self.driver.find_element_by_tag_name('mg-change-receiver-location').click()
        time.sleep(2)
        print('return back to caller')
        return exchange_rate

    def parse_country_list(self, response):
        print('url: {}'.format(self.start_urls))
        self.driver.implicitly_wait(30)
        self.driver.get(response.url)

        # select the dropdown button once it is availble
        # dropdown = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="smonewuser"]/div/app-sendmoney-option/div[2]/div[1]/div/div/form/app-country-dropdown/div/ul')))

        # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='smonewuser']/div/app-sendmoney-option//span[text()='United States]"))).click()

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
