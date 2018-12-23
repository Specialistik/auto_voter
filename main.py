# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

HEADERS_CHROME = {
    "content-type":"text/html; charset=utf-8", 
    "x-requested-with": "XMLHttpRequest",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
}

def account_generator():
    with open('vk_accounts.txt') as vk_accs:
        for vk_acc in vk_accs:
            vk_email, vk_pass = vk_acc.split(':')
            yield vk_email, vk_pass.rstrip('\n')

r = requests.get('https://www.business-gazeta.ru/article/406831', headers={"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"})
beautiful = BeautifulSoup(r.text)
with open('response.html', 'w') as response_file:
    response_file.write(beautiful.text)
for link in beautiful.find_all("input", type="hidden"):
    post_request_data = {
        'variant': 148252,
        'poll': 2519,
    }
    #if link['name'] in ['csrf', ]
    print link['name'], link['value']
    #print(link.name, link.text)
#print r.status_code

#r2 = requests.post("https://www.business-gazeta.ru/article/406831/polls/ajax/method/vote",  headers=HEADERS_CHROME)
#print r2.text
#lolka = BeautifulSoup(r2.text)
#print lolka.prettify()
#print r.body
#print r.text