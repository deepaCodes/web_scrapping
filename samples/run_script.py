# -*- coding: utf-8 -*-
import json
import time
import requests
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

"""
pip install selenium-wire

"""

api_ends_with = '/api/v2/collector'
cookie_key = '_px3'

# https://www.finishline.com/store/

class ExecuteScript():
    headless_browser = True
    api_ends_with = '/api/v2/collector'
    cookie_key = '_px3'

    def __init__(self):
        self.driver = self.initialize_web_driver()
        self.url = 'https://www.google.com/'
        self.js_script_url = 'https://www.ubiqlife.com/SB9qOXXg/init.js'

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
        print('starting script execution')
        self.driver.get(self.url)
        time.sleep(5)
        js_content = requests.get(self.js_script_url).text
        print('got js content from: {}'.format(self.js_script_url))
        self.driver.execute_script(js_content)
        print('JS script executed')
        time.sleep(30)
        # Access requests via the `requests` attribute
        # result = [json.loads(req.response.body.decode("utf-8")) for req in self.driver.requests if '/api/v2/collector' in req.path and req.response]
        result = [cookie_str for xhr_resp in
                  [json.loads(req.response.body.decode("utf-8"))['do'] for req in self.driver.requests if
                   api_ends_with in req.path and req.response] for cookie_str in xhr_resp if cookie_key in cookie_str]
        #print(result)
        print('cookie string')
        for cookie in result:
            print(cookie)

        self.driver.quit()
        print('end of script')


if __name__ == '__main__':
    script = ExecuteScript()
    script.start_requests()
