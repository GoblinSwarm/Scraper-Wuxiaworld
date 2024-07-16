# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 21:59:36 2024

@author: Light
"""

from datetime import datetime


def get_name(url):
    
    name_begins_with=url.rfind('/')
    name=url[name_begins_with+1:]
    
    return name

def main(url):

    try:
        log_file='wuxiaworld-click.csv'
        timestamp_format = '%Y-%h-%d-%H:%M:%S' 
        now = datetime.now() # get current timestamp 
        timestamp = now.strftime(timestamp_format) 
        name=get_name(url)
        name=name.replace('-',' ')
        name=name.capitalize()
        with open(log_file,"a") as f: 
            f.write(timestamp + ',' + url + ',' + name + '\n') 
        
    except Exception as e:
        print('Something bad happened at log.' , e)
        
        
    