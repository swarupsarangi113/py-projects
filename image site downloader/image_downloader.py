import requests
from bs4 import BeautifulSoup


URL = 'https://www.flickr.com/search/?text=cats'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

source = requests.get(URL, headers=headers).text

soup = BeautifulSoup(source, 'lxml')

for card in soup.find_all("div",class_='view photo-list-photo-view requiredToShowOnServer awake') :

    href_tag = card.find("a",class_='overlay')
    print(href_tag)