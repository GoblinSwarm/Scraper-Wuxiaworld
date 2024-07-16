# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 21:02:34 2024

@author: Light
"""

import requests
from bs4 import BeautifulSoup
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def chapter_exists(chapter):
    
    minimun_to_exist=300
    if len(chapter) < minimun_to_exist:
        return False
    return True

def main(url):
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
    
        soup = BeautifulSoup(response.text, 'html.parser')
    
        # Extract any desired information from the HTML using BeautifulSoup
        # For demonstration, let's extract the title of the webpage
        title = soup.title.string
        chapter= soup.get_text()
        
        if chapter_exists(chapter) == True:
            # Create a dictionary to store the data
            data = {'url': url, 'title': title, 'chapter': chapter}
            
            return(data)
            
        else:
            
            return None
        
    else:
        print("Failed to retrieve data from the URL")

    response.close()