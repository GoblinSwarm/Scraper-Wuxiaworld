# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 23:57:11 2024

@author: Light
"""
import os

def main(data):

    title=data['title']
    title = data['title'].replace("'", '').replace("?", '').replace(":", '').replace("/", '')

    find_position=title.find('-')
    title=title[:find_position]
    
    chapter=data['chapter']
    
    folder=data['url']
    
    find_pos=folder.rfind('-')
    folder=folder[:find_pos]
    
    find_root=folder.rfind('/')
    folder=folder[find_root+1:]
    folder=folder.replace('-', ' ')
    folder=folder.capitalize()
    
    chapter_title= title + '.txt'
    
    file_path = os.path.join(folder, chapter_title)
    os.makedirs(folder, exist_ok=True)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(chapter+'\n')