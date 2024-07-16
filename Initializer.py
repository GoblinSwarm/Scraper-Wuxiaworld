# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 22:17:14 2024

@author: Light
"""

import get_links as crawler
import get_text_inJson as reader
import log_wuxia as log
import writer
from datetime import datetime


def time():
    timestamp_format = '%Y-%h-%d-%H:%M:%S' 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    
    return  timestamp  

url=input("Por favor, ingresa la url del wuxia a Scrapear: ")

if url == '':
    url='https://wuxia.click/chapter/unrivaled-medicine-god-1'
    
    
forward=True
while forward == True:
    timestamp=time()
    print(url, timestamp)
    data=reader.main(url)
    if data != None:
        log.main(url)
        writer.main(data)
        url=crawler.main(url)
    else:
        forward=False
    
print('Last chapter reached')
