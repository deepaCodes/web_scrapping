import json

text = "window.__env.clientKey =" \
       "       "'Basic V0VCX2VkYjI0ZDc5LTA0ODItNDdlMi1hNmQ2LTc4ZGY5YzI4MmM0ZTo1MTNlMTEyOS0yZTJmLTRlYmUtYjkwMi02YTVkMGViMDNjZjc=';

import re

print(text)
pattern = re.compile(r"window.__env.clientKey =*?;")
match = re.match(r'window.__env.clientKey =*?;', text)
print(pattern.findall(text))

import requests

response = requests.get('https://consumerapi.moneygram.com/services/capi/api/v1/config/countries',
                        headers={'Accept': 'application/json',
                                 'clientkey': 'Basic V0VCX2VkYjI0ZDc5LTA0ODItNDdlMi1hNmQ2LTc4ZGY5YzI4MmM0ZTo1MTNlMTEyOS0yZTJmLTRlYmUtYjkwMi02YTVkMGViMDNjZjc='}, )

print(response.json())

print(response.json()['countryList'])

country_list = []
for country in response.json()['countryList']:
    print(country)
    if not country['sendActive']:
        continue
    country_list.append({'code': country['code'], 'iso2Code': country.get('iso2Code', None), 'name': country['name'],
                         'baseReceiveCurrency': country.get('baseReceiveCurrency', None),
                         'sendCurrencies': country['sendCurrencies'][0]
                         })

    print(country_list)


with open('E:/python/web_scrapping/DATA/country.json', encoding='utf-8') as f:
    country_list = json.load(f)

print('countries: {}'.format(country_list))