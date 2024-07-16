# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 21:05:37 2024

@author: Light
"""

import requests
from bs4 import BeautifulSoup
import json
import re


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def get_next_chapter(possible_chapters):
    
    if len(possible_chapters) == 1:
        next_chapter=str(possible_chapters)
        
    else:
        #Spliting the list, like a madman!
        prev_chap=possible_chapters[0]
        next_chap=possible_chapters[1]    
        
        #Singaling where to look for numbers
        prev=prev_chap.rfind('-')
        nxt=next_chap.rfind('-')
        
        #Picking the numbers
        first_number=prev_chap[prev+1:]
        last_number=next_chap[nxt+1:]
        #Casting them
        first_number=int(first_number)
        last_number=int(last_number)
        
        if first_number > last_number:
            next_chapter=prev_chap
        else:
            next_chapter=next_chap
        
    next_chapter=next_chapter.replace("'",'')
    next_chapter=next_chapter.replace('[','')
    next_chapter=next_chapter.replace(']','')
    
    return next_chapter


def main(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all anchor tags (links) in the webpage
        links = soup.find_all('a', href=True)
        
        # Extract URLs from anchor tags
        urls = [link['href'] for link in links]
        
        # Filter out URLs that are None or empty strings
        urls = filter(None, urls)
    
        # Convert URLs to a list and remove duplicates
        urls = list(set(urls))

        possible_chapters=[]
        for element in urls: 
            if '/chapter/' in element:
                possible_chapters.append(element)
    
        next_chapter=get_next_chapter(possible_chapters)
        domain_pos=url.find('/chapter/')
        domain=url[:domain_pos]
        next_chapter=domain+next_chapter
        
        return next_chapter
            
    else:
        print("Failed to retrieve data from the URL")

    response.close()