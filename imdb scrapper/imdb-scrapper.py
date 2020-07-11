# scraps the imdb top charts
import requests
from bs4 import BeautifulSoup

source = requests.get("https://www.imdb.com/chart/top/").text

soup = BeautifulSoup(source, 'lxml')
tbody = soup.find("tbody", class_="lister-list")

for tr in tbody.find_all("tr") :

    title = tr.find("td", class_="titleColumn").a.text
    rating = tr.find("td", class_="ratingColumn imdbRating").strong["title"]
    href_link = tr.find("td", class_="titleColumn").a["href"]
    link = "https://www.imdb.com/"+href_link

    src = requests.get(link).text
    new_soup = BeautifulSoup(src,'lxml')
    plot_summary = new_soup.find("div",class_="plot_summary").div.text.strip()

    print("Title-", title)
    print("Rating-", rating)
    # print("link-",link)
    print("Summary-",plot_summary+'\n')
    
    