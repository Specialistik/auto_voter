# -*- coding: utf-8 -*-
import requests
import os
import time
import random
from bs4 import BeautifulSoup

def account_generator():
    with open('vk_accounts.txt') as proxy_accs:
        for proxy_acc in proxy_accs:
            yield proxy_acc.rstrip('\n')


for i in account_generator():
    bash_command = "casperjs casperas.js --proxy=" + i
    print "--------------new casper command : " + bash_command
    os.system(bash_command)
    random_secs = random.randint(3,30)
    print "---------------------sleep for " + str(random_secs)
    time.sleep(random_secs)
