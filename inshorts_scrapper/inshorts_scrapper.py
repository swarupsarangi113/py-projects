# extracts news headlines from the inshorts dashboard
import requests
import webbrowser
import bs4

res = requests.get("https://inshorts.com/en/read")

# print(res.status_code)
try:
    res.raise_for_status()
except Exception:
    print("Something Went Wrong !")

soup = bs4.BeautifulSoup(res.text, 'html.parser')

newscards = soup.select(".news-card.z-depth-1")

for card in newscards:
    a_tag = card.find("a")

    #this portion to open all the links in the browser
    href_tag = a_tag.attrs["href"]
    urlToOpen = "https://inshorts.com"+href_tag
    webbrowser.open(urlToOpen)

    #shows the headlines of the page in CL
    span_tag = a_tag.find("span")
    print(span_tag.text)
    print()
