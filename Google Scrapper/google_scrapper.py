# a python script to google search and automaically open the first 5 results in new tab

import requests
from bs4 import BeautifulSoup
import webbrowser
import sys


def google_scrap():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

    try:
        URL = "https://www.google.com/search?q={}".format(sys.argv[1])
    except Exception:
        print("Run the script along with a string\nhint: python google_scrapper.py 'cricket 2020' ")
        sys.exit()

    source = requests.get(URL, headers=headers).text
    soup = BeautifulSoup(source, 'lxml')

    searches = soup.find_all("div", class_="rc")
    no_of_searches = len(searches)

    for i in range(min(5, no_of_searches)):
        href_tag = searches[i].find("a")['href']
        print(href_tag)
        webbrowser.open(href_tag)


google_scrap()
