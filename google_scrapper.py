# a python script to google search and automaically open the first 5 results in new tab

import requests
from bs4 import BeautifulSoup
import webbrowser
import sys

if len(sys.argv) > 1 :
    URL = "https://www.google.com/search?q={}".format(sys.argv[1])
else :
    print("Please enter a string to search")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

source = requests.get(URL, headers=headers).text

soup = BeautifulSoup(source, 'lxml')

searches = soup.find_all("div", class_="rc")
no_of_searches = len(searches)

for i in range(min(5,no_of_searches)):
    href_tag = searches[i].find("a")['href']
    webbrowser.open(href_tag)
