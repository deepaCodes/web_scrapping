# -*- coding: utf-8 -*-
from threading import Thread

import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait


class MoneygramSpider(scrapy.Spider):
    name = 'moneygram'
    allowed_domains = ['www.moneygram.com']
    start_urls = [
        'https://www.moneygram.com/mgo/us/en/?gclid=EAIaIQobChMI2ebola3a5wIVgpyzCh3uHAsUEAAYASAAEgJcufD_BwE/']

    custom_settings = {
        'RETRY_ENABLED': False
    }

    headless = True

    def __init__(self):
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path='E:/chromedriver_win32/chromedriver.exe', chrome_options=chrome_options)
        print('got driver')

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse_exchange_rate, errback=self.failure, dont_filter=True)
            # yield scrapy.Request(url, callback=self.parse_country_list, errback=self.failure, dont_filter=True)

    def parse_exchange_rate(self, response):
        print('url: {}'.format(self.start_urls))
        self.driver.implicitly_wait(10)
        self.driver.get(response.url)
        _selector = self.driver.find_element_by_xpath('//*[@id="mat-tab-label-0-0"]/div')
        print('Exchange Rate:\n{}'.format(_selector.text))

        #print response.body
        send = self.driver.find_element_by_xpath('//*[@id="send"]')
        #WebDriverWait(self.driver, 10).until(EC.visibility_of(send)).click()
        #send.click()
        send.clear()
        send.send_keys('1')
        print('amount updated')

        self.driver.implicitly_wait(10)

        receiveCountry = self.driver.find_element_by_xpath('//*[@id="receiveCountry"]')
        #receiveCountry.click()
        #WebDriverWait(self.driver, 10).until(EC.visibility_of(receiveCountry)).click()
        receiveCountry.clear()
        receiveCountry.send_keys('India')
        print('country updated')

        self.driver.implicitly_wait(10)
        #sleep(10)
        self.driver.find_element_by_xpath('//*[@id="mat-dialog-0"]/mg-dialog/div/mat-icon').click()
        self.driver.find_element_by_xpath('//*[@id="mat-dialog-0"]/mg-dialog/div/mat-icon').click()

        while True:
            #sleep(5)
            try:
                #result = self.driver.find_element_by_xpath('//*[@id="startEstimate"]').click()
                element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="startEstimate"]')))

                element.click()
                print('button clicked')
            except:
                print('except block')
                break

        exchange_rate = wait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-tab-content-0-0"]/div/mg-estimate-view/div/mg-exchange-rate/div')))

        #exchange_rate = self.driver.find_element_by_xpath('//*[@id="mat-tab-content-0-0"]/div/mg-estimate-view/div/mg-exchange-rate/div')
        print(exchange_rate.text)
        print('Receiving country: India, exchange rate: {}'.format(exchange_rate.text))
        print('done')
        return None

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
