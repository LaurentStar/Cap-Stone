from bs4 import BeautifulSoup
import datetime
import json
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import requests
import time
from html.parser import HTMLParser
import lxml
from lxml.html.clean import Cleaner
import re
from random import randint

def clean_me(url):
    if randint(0, 11) > 8:
        time.sleep(1)
        
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    }
    try:
        html  = requests.get(url, headers=headers).text
    except:
        return 'none'
    
    soup = BeautifulSoup(html, "html.parser") # create a new bs4 object from the html data loaded
    for script in soup(["script", "style"]): # remove all javascript and stylesheet code
        script.extract()
    # get text
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    text = text.replace('\n', ' ')
    text = text.replace('|', ' ')
    return text

_  = os.path.join('data', 'buzzfeed_2018_fake_news.csv')
buzz_feed_fakenews_df = pd.read_csv(_)


outF = open("data.txt", "a", encoding="utf-8") 
for index, value in enumerate(buzz_feed_fakenews_df['url'][7115:]): 
    
    outF.write(clean_me(value)) 
    outF.write("\n")
    if index%100 == 0:
        print(datetime.datetime.now(), 'index', index)
        
outF.close()        
        
        
buzz_feed_fakenews_df['article'] = pd.Series[tmp]
buzz_feed_fakenews_df.to_csv('test.')