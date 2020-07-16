import numpy as np
import pandas as pd
import sys
import re
import codecs
import requests
from bs4 import BeautifulSoup


vgm_url = 'https://www.vgmusic.com/music/console/nintendo/nes/'
html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, 'html.parser')
# to print with html tag
# print(soup)
# to print the title of the page
print(soup.title)
# title text
print(soup.title.text)

# to print text of the page
print(soup.get_text())

# # To print the only one element we know: here banner_ad
print(soup.find(id='banner_ad'))
print(soup.find(id='banner_ad').text)

sys.exit(0)
# To print all the
for link in soup.find_all('a'):
    print(link.get('href'))


sys.exit(0)
# our thing: html file reading
with open('new_doc.html','r') as f:
    con = f.read()
    soup = BeautifulSoup(con, 'lxml')
print(soup)
print('*'*20)
# print(soup.get_text())
print(soup.find('p').text)

