import glob
import io
import os
import time
import traceback
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path
import requests
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyodbc
import json
import pathlib

try:
    from PIL import Image
except ImportError:
    import Image

headless = True
DOWNLOAD_DIR = str(os.path.join(Path.home(), "Downloads"))
CURRENT_DIR = pathlib.Path(__file__).parent.absolute()
config = {}


def init_config():
    print('initializing config')
    with open('{}/config.json'.format(CURRENT_DIR)) as json_file:
        data = json.load(json_file)

    config.update(data)
    pytesseract.pytesseract.tesseract_cmd = '{}/tesseract'.format(config.get('tesseract_path'))
    os.environ["TESSDATA_PREFIX"] = "{}/tessdata".format(config.get('tesseract_path'))
    # print(config)


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))
    return ''.join(text.split())


def predict_captcha(captcha_img_url):
    print('predictng captcha')

    response = requests.get(captcha_img_url, verify=False)
    img_buffer = response.content
    # print(img_buffer)
    img = Image.open(io.BytesIO(img_buffer))
    # img.save('predict_images/request.jpg')
    text = pytesseract.image_to_string(img)
    # print(text.split())
    print('predict digits: {}'.format(text))

    return text


def predict_captcha_from_buffer(img_buffer):
    print('predictng captcha from img_buffer')
    img = Image.open(io.BytesIO(img_buffer))
    # img.save('predict_images/request.jpg')
    text = pytesseract.image_to_string(img)
    # print(text.split())
    print(text)
    return ''.join(text.split())


def enable_download_in_headless_chrome(driver, download_dir):
    """
    there is currently a "feature" in chrome where
    headless does not allow file download: https://bugs.chromium.org/p/chromium/issues/detail?id=696481
    This method is a hacky work-around until the official chromedriver support for this.
    Requires chrome version 62.0.3196.0 or above.
    """

    print('Enable download in headless mode')
    # add missing support for chrome "send_command"  to selenium webdriver
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    command_result = driver.execute("send_command", params)
    print("response from browser:")
    for key in command_result:
        print("result:" + key + ":" + str(command_result[key]))


def init_webdriver():
    options = Options()

    # options.add_argument("--start-maximized")
    # options.add_argument("--no-startup-window")
    """
    options.add_argument("--incognito")
    options.add_argument("--dns-prefetch-disable")
    #options.add_argument("--window-size=100,100")
    """
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--ignore_ssl")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--log-level=3")

    if DOWNLOAD_DIR:
        prefs = {'download.default_directory': DOWNLOAD_DIR,
                 "download.prompt_for_download": False,
                 "download.directory_upgrade": True,
                 "safebrowsing_for_trusted_sources_enabled": False,
                 "safebrowsing.enabled": False,
                 }

        options.add_experimental_option('prefs', prefs)

    if headless:
        options.add_argument("--headless")

    driver = webdriver.Chrome(executable_path=config.get('chromedriver_path'), options=options)

    if headless:
        enable_download_in_headless_chrome(driver, DOWNLOAD_DIR)

    # driver.minimize_window()
    print('got driver')

    # enable_download_in_headless_chrome(driver, DOWNLOAD_DIR)

    return driver


def predict_test():
    files = glob.glob(os.path.join('predict_images', "*.jpg"))
    for file in files:
        print(file)
        print(ocr_core(file))


def download_tx_csv(driver):
    """
    :param driver:
    :return:
    """

    driver.get(config.get('ezpass_login_url'))
    # driver.minimize_window()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//form[@name="accountLoginForm"]//img[@class="imgcap"]')))

    captcha_img_file = 'captcha.png'
    with open(captcha_img_file, 'wb') as file:
        file.write(
            driver.find_element_by_xpath('//form[@name="accountLoginForm"]//img[@class="imgcap"]').screenshot_as_png)

    captcha_digits = ocr_core(captcha_img_file)
    print('captcha_digits: {}'.format(captcha_digits))

    user_name = driver.find_element_by_id('tt_username1')
    password = driver.find_element_by_id('tt_loginPassword1')
    jcaptcha_input = driver.find_element_by_id('jcaptcha_response1')

    # send input data
    user_name.send_keys(config.get('username'))
    time.sleep(1)
    password.send_keys(config.get('password'))
    time.sleep(1)
    jcaptcha_input.send_keys(captcha_digits)
    time.sleep(2)

    sign_in = driver.find_element_by_xpath('//form[@name="accountLoginForm"]//button[@name="btnLogin"]')
    sign_in.click()

    print('going to login')

    # check for errors

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="toll_transactions_wrapper"]')))
    print('login success')

    # account_tx_link = 'https://www.ezpassnj.com/vector/account/transactions/batatransactionSearch.do'
    # csv_url ='https://www.ezpassnj.com/vector/account/transactions/batatransactionSearch.do?printType=xls&exclGen=true'
    # driver.get(account_tx_link)

    time.sleep(5)
    tx_link = driver.find_element_by_xpath('//*[@id="sb-site"]/div[3]/div/div/form/div[6]/div[1]/div/a')
    tx_link.click()

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//table[@id="transactionItem"]')))

    df = scrape_table(driver)
    # df = download_csv(df, driver)

    print(df.count())
    print(df.to_string())
    return df


def save_to_access_db(df):
    """
    https://www.microsoft.com/en-us/download/confirmation.aspx?id=13255
    https://www.microsoft.com/en-us/download/confirmation.aspx?id=54920
    :param df:
    :return:
    """
    print('saving to access database')
    print(pyodbc.version)
    print('available drivers: {}'.format(pyodbc.drivers()))
    print('odbc string: {}'.format(config.get('odbc_driver')))
    conn = pyodbc.connect(config.get('odbc_driver'))
    df.to_sql('nj_ez_pass', conn, if_exists='append')
    print('data saved to ms access db')


def download_csv(driver):
    print('downloading link ')
    time.sleep(2)
    download_link = driver.find_element_by_xpath('//*[@id="searchForm"]/div/div/div/div[5]/div/a[2]')
    download_link.click()
    time.sleep(5)
    files = glob.glob(DOWNLOAD_DIR + "/*.csv")
    files.sort(key=os.path.getmtime)
    latest_csv_file = files[-1]
    print('file name: {}'.format(latest_csv_file))
    df = pd.read_csv(latest_csv_file)
    return df


def scrape_table(driver):
    soup = BeautifulSoup(driver.page_source, 'lxml')
    headers = [th_el.text for th_el in soup.findAll('table')[2].findAll('th')]
    print('headers: {}'.format(headers))
    rows = []
    for tr_el in soup.findAll('table')[2].findAll('tr')[1:]:
        row = [td_el.text for td_el in tr_el.findAll('td')]
        # print(row)
        rows.append(row)

    # print(rows)
    df = pd.DataFrame(data=rows, columns=headers)
    df['Description'] = df['Description'].str.strip()

    return df


def scrape_ezpass():
    """
    scrape ezpass tx list
    :return: status
    """
    init_config()
    status_flag = False
    try:
        for counter in range(0, 5):
            print('Trial: {}'.format(counter + 1))
            try:
                driver = init_webdriver()
                df = download_tx_csv(driver)
                df.to_csv('result_{}.csv'.format(time.strftime("%Y%m%d-_H%M%S")))
                save_to_access_db(df)
                status_flag = True
                break
            except Exception as ex:
                print('Exception block')
                print(ex)
                for elem in driver.find_elements_by_xpath(
                        '//div[@id="sb-site"]//div[@class="alert alert-danger error_msg"]'):
                    print(elem.text)

                for elem in driver.find_elements_by_xpath('//div[@id="jcaptcha_response"]'):
                    print(elem.text)

                print(traceback.format_exc())
            finally:
                driver.close()
            time.sleep(10)
        print('end of script')
    finally:
        print('cleanup any resources')

    return status_flag


if __name__ == '__main__':
    print('Main entry program')
    success = scrape_ezpass()
    """
    for i in range(0, 3):
        print('Main trail: {}'.format(i + 1))
        success = scrape_ezpass()
        if success:
            break

        # wait for 10sec before trying
        time.sleep(10)
    """
