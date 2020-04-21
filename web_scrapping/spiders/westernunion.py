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


# https://www.westernunion.com/us/en/web/send-money/start?SrcCode=12345&ReceiveCountry=US&SendAmount=100&ISOCurrency=CNY&FundsOut=BA&FundsIn=CreditCard

# https://www.westernunion.com/us/en/web/send-money/start?SrcCode=12345&ReceiveCountry=BG&SendAmount=100&FundsOut=CP&FundsIn=CreditCard
class WesternUnionSpider(scrapy.Spider):
    name = 'western_union'
    allowed_domains = ['www.westernunion.com']
    # start_urls = ['https://www.westernunion.com/us/en/web/send-money/start/']

    start_urls = [
        'https://www.westernunion.com/us/en/web/send-money/start?SrcCode=12345&ReceiveCountry=IN&SendAmount=100']

    custom_settings = {
        'RETRY_ENABLED': False
    }

    headless_browser = False
    exclude_country = ['United States']

    def __init__(self):
        self.driver = self.initialize_web_driver()

    def initialize_web_driver(self):
        # Add additional Options to the webdriver
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--incognito")
        # chrome_options.add_argument("--kiosk")
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
            # yield scrapy.Request(url, callback=self.parse_exchange_rate, errback=self.failure, dont_filter=True)
            # yield scrapy.Request(url, callback=self.parse_country_list, errback=self.failure, dont_filter=True)
            yield scrapy.Request(url, callback=self.parse_wu, errback=self.failure, dont_filter=True)

    def parse_wu(self, response):
        print('url: {}'.format(response.url))
        code_list = ['IN', 'AF', 'AL', 'BS', 'CN', 'PH', 'MX', 'CO', 'JM']
        for code in code_list:
            try:
                _url = 'https://www.westernunion.com/us/en/web/send-money/start?SrcCode=12345&ReceiveCountry={}&SendAmount=100'.format(
                    code)
                print('opening url: {}'.format(_url))
                self.driver.get(_url)
                self.driver.implicitly_wait(5)

                # web driver wait
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "fundsOut_AG")))
                sleep(2)

                _selector = self.driver.find_element_by_xpath('//*[@id="smoExchangeRate"]')
                print('Exchange Rate:\n{}'.format(_selector.text))

                sleep(3)
                print('completed')

            except Exception as ex:
                print('exception block')
                print(ex)
            finally:
                print('finally')
                # self.driver.close()

        self.driver.quit()

    def parse_exchange_rate(self, response):
        print('url: {}'.format(self.start_urls))

        try:
            self.driver.get(response.url)
            self.wait_for_page_load()

            # har = json.loads(self.driver.get_log('browser')[0]['message']) # get the log
            # print('headers: ', har['log']['entries'][0]['request']['headers'])
            print(self.driver.get_log('browser'))
            print(self.driver.get_log('driver'))
            print(self.driver.get_log(None))

            # Step 1: Create a parse tree of page sources after searching
            soup = BeautifulSoup(self.driver.page_source, "lxml")

            country_list = [div.text for div in soup.find_all("span", {'class': 'hy-country'})]
            print(country_list)

            _selector = self.driver.find_element_by_xpath('//*[@id="smoExchangeRate"]')
            print('Exchange Rate:\n{}'.format(_selector.text))

        except Exception as ex:
            print('Exception')
            print(ex)
        finally:
            print('closing driver. top')
            # closing the current window
            self.driver.quit()

        country_codes = ['IN', 'BG', 'BR', 'AF']
        for _code in country_codes:
            try:
                # sleep(randint(1, 3))
                self.driver = self.initialize_web_driver()
                send_amount = randint(500, 1000)
                # _start_url = 'https://www.westernunion.com/us/en/web/send-money/start?ReceiveCountry={}&SendAmount={}'
                _start_url = 'https://www.westernunion.com/us/en/web/send-money/start?SrcCode=12345&ReceiveCountry={}&SendAmount={}&FundsOut=CP&FundsIn=CreditCard'
                _url = str(_start_url).format(_code, send_amount)
                print('opening url: {}'.format(_url))

                self.driver.get(_url)
                self.wait_for_page_load()

                # sleep(randint(2, 5))
                _selector = self.driver.find_element_by_xpath('//*[@id="smoExchangeRate"]')
                print('Exchange Rate:\n{}'.format(_selector.text))

                yield {'rate': _selector.text}
            except Exception as ex:
                print('Exception')
                print(ex)
            finally:
                print('closing driver')
                self.driver.quit()
        """
        sleep(5)
        country_menu = self.driver.find_element_by_id("country")
        country_menu.click()
        #country_menu.send_keys('India')
        sleep(2)
        country_menu.send_keys(Keys.ENTER)
        #//*[@id="country"]
        #//*[@id="exchangeRate"]

        WebDriverWait(self.driver, 5).until(
            lambda s: s.find_element_by_id("exchangeRate").is_displayed()
        )

        sleep(5)
        _selector = self.driver.find_element_by_xpath('//*[@id="smoExchangeRate"]')
        print('Exchange Rate:\n{}'.format(_selector.text))
        
        """

    def parse_country_list(self, response):
        print('url: {}'.format(self.start_urls))
        self.driver.get(response.url)
        self.wait_for_page_load()

        # Step 1: Create a parse tree of page sources after searching
        soup = BeautifulSoup(self.driver.page_source, "lxml")

        country_list = [div.text for div in soup.find_all("span", {'class': 'hy-country'})]
        print(country_list)

        # select the dropdown button once it is availble
        # dropdown = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="smonewuser"]/div/app-sendmoney-option/div[2]/div[1]/div/div/form/app-country-dropdown/div/ul')))

        # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='smonewuser']/div/app-sendmoney-option//span[text()='United States]"))).click()

        # search all options
        # options = self.driver.find_elements_by_css_selector(".hy-country-container .hy-country")
        # print all option text

        # _selector = self.driver.find_element_by_class_name('dropdown-menu')
        # print('Country List:\n{}'.format(options))
        return country_list

    def wait_for_page_load(self):
        WebDriverWait(self.driver, randint(5, 10)).until(
            lambda s: s.find_element_by_id("button-fraud-warning-accept").is_displayed()
        )
        self.driver.find_element_by_id('button-fraud-warning-accept').click()

        """
        WebDriverWait(self.driver, randint(5, 10)).until(
            lambda s: s.find_element_by_id("exchangeRate").is_displayed()
        )
        """

        sleep(randint(3, 5))

    def failure(self, failure):
        # log all failures
        self.logger.error(repr(failure))
        item = {}
        item['Web Address'] = failure.request.url
        print('item: {}'.format(item))
        yield None

    def _dead_code(self):
        # web driver wait
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "button-top-ban-send-money")))
        sleep(2)
        element.click()
        sleep(2)

        type_ahead = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "country")))
        sleep(2)

        ele = self.driver.find_element_by_xpath('//*[@id="top-country-tile"]/div/button[3]')
        sleep(1)
        ele.click()
        sleep(10)

        if False:
            ele = self.driver.find_element_by_xpath("//div[@role='search']")
            sleep(2)
            ele.click()
            type_ahead.send_keys(Keys.NULL)
            # type_ahead.click()
            sleep(2)
            type_ahead.clear()
            sleep(2)
            type_ahead.send_keys("India")
            # sleep(2)
            # type_ahead.send_keys(Keys.ARROW_DOWN)

            items = self.driver.find_elements_by_xpath(
                '//*[@id="smonewuser"]/div/app-sendmoney-option/div[2]/div[1]/div/div/form/app-country-dropdown/div[1]/ul/li/a')
            for item in items[1:2]:
                print(item)
                print(item.text)
                item.click()
