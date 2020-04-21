# -*- coding: utf-8 -*-
import json
import time

from selenium.webdriver import DesiredCapabilities
from seleniumwire import webdriver

from selenium.webdriver.chrome.options import Options as ChromeOptions, Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
"""
pip install selenium-wire

"""

api_starts_with = 'https://www.finishline.com/public'
cookie_key = '_px3'

# https://www.finishline.com/store/

class ExecuteScript():
    headless_browser = False

    def __init__(self):
        self.driver = self.initialize_web_driver()
        self.url = 'https://www.finishline.com/store/'
        #self.url = 'https://www.google.com/store/'

    def initialize_web_driver(self):
        # Add additional Options to the webdriver
        chrome_options = ChromeOptions()
        # add the argument and make the browser Headless.
        if self.headless_browser:
            chrome_options.add_argument("--headless")

        """
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--kiosk")
        """

        # set options
        """
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--proxy-server='direct://'")
        chrome_options.add_argument("--proxy-bypass-list=*")
        chrome_options.add_argument("--start-maximized")
        """
        driver = webdriver.Chrome(executable_path='E:/chromedriver_win32/chromedriver.exe', options=chrome_options)
        print('got driver')
        return driver

    def firefox_driver(self):
        options = Options()
        options.add_argument("--headless")
        binary = FirefoxBinary('C:/Program Files (x86)/Mozilla Firefox/firefox.exe')
        options.binary = binary

        fp = (r'C:\Users\username\AppData\Roaming\Mozilla\Firefox\Profiles\oqmqnsih.default')
        options.profile = fp
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = False

        #driver = webdriver.Firefox(executable_path='E:/geckodriver-v0.26.0-win64/geckodriver.exe',capabilities=cap, options=chrome_options)
        driver = webdriver.Firefox(executable_path='E:/geckodriver-v0.26.0-win64/geckodriver.exe', firefox_options=options)
        print('got driver')
        return driver

    def start_requests(self):
        print('starting script')
        self.driver.get(self.url)
        # web driver wait
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, "home_c")))
        #time.sleep(20)
        # Access requests via the `requests` attribute
        # result = [json.loads(req.response.body.decode("utf-8")) for req in self.driver.requests if '/api/v2/collector' in req.path and req.response]
        result = [req for req in self.driver.requests if str(req.method).upper() == 'POST' and api_starts_with in req.path]

        for req in reversed(result):
            print(req)

        sensor_data = None
        response = None
        headers = None
        for req in reversed(result):
            print(req)
            if req.response and req.response.body and json.loads(req.response.body)['success'] == True:
                print('Valid sensor data')
                headers = req.headers
                response = json.loads(req.response.body)
                sensor_data = json.loads(req.body)['sensor_data']
                break

        print('headers: {}'.format(headers))
        print('response: {}'.format(response))
        print('sensor_data: {}'.format(sensor_data))
        print('cookie:\n{}'.format(headers['Cookie']))
        for cookie_str in str(headers['Cookie']).split(';'):
            print(cookie_str)

        self.driver.quit()
        print('end of script')


if __name__ == '__main__':
    script = ExecuteScript()
    script.start_requests()
