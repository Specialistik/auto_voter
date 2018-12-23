# -*- coding: utf-8 -*-
import requests
import os
import time
import random
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def account_generator():
    with open('vk_accounts.txt') as proxy_accs:
        for proxy_acc in proxy_accs:
            yield proxy_acc.rstrip('\n')


for i in account_generator():
    bash_command = "casperjs casperas.js --proxy=" + i
    print "------------------------new proxy command"
    os.system(bash_command)
    print "---------------------sleep for 10 seconds"
    time.sleep(random.randint(3,60))
    
#r = requests.get('https://www.business-gazeta.ru/article/406831', headers={"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"})
#beautiful = BeautifulSoup(r.text)
#with open('response.html', 'w') as response_file:
#    response_file.write(beautiful.text)

"""
for iteration, link in enumerate(beautiful.find_all("input", type="hidden")):
    post_request_data = {
        'variant': 148252,
        'poll': 2519,
        'local_ip': "192.168.1.9",
    }
    if link['name'] == 'csrf':
        post_request_data['csrf'] = link['value']
    if iteration == 2:
        post_request_data[link['name']] = 
        print iteration, link['name'], link['value']
    #print(link.name, link.text)
"""