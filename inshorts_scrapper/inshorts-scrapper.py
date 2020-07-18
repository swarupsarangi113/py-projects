import requests
from bs4 import BeautifulSoup
import webbrowser

source = requests.get("https://inshorts.com/en/read").text

soup = BeautifulSoup(source, 'lxml')

for news_card in soup.find_all("div", class_="news-card z-depth-1") :

    headline = news_card.a.span.text
    summary = news_card.find("div", class_ = "news-card-content news-right-box").div.text
    link = "https://inshorts.com" + news_card.a['href']

    #write into a txt file
    # with open('news.txt','a') as f :

    #     f.writelines('{}\n {}\n Link - {}\n\n\n'.format(headline,summary,link))

    print(headline,'\n')
    print(summary,'\n')
    print(link,'\n')

    # #Uncomment this to open all the links in browser
    # # webbrowser.open("https://inshorts.com"+link)
    # print()