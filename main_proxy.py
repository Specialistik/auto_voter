# -*- coding: utf-8 -*-
import requests
import os
import time
import random
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.sql import select

engine = create_engine("mysql://root:1f53601c@localhost/business_gazeta")
db_connection = engine.connect()

def account_generator():
    with open('proxy_accs.txt') as proxy_accs:
        for proxy_acc in proxy_accs:
            yield proxy_acc.rstrip('\n')

def random_user_agent_generator():
    return 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'

for i in account_generator():
    bash_command = "casperjs casperas.js --proxy=" + i
    print "--------------new casper command : " + bash_command
    os.system(bash_command)
    random_secs = random.randint(3,30)
    print "---------------------sleep for " + str(random_secs)
    time.sleep(random_secs)
