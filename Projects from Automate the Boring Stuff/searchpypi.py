import sys,pyperclip,bs4,webbrowser,requests

def search_pypi() :
    '''
    This is what your program does:
    1. Gets search keywords from the command line arguments
    2. Retrieves the search results page
    3. Opens a browser tab for each result
    '''
    if len(sys.argv) > 1 :
        search = sys.argv[1].replace(' ','+')
    else :
        search = pyperclip.paste().replace(' ','+')
    
    res = requests.get("https://pypi.org/search/?q={}".format(search))
    try :
        res.raise_for_status()
    except Exception :
        print('there was some problem...')

    soup = bs4.BeautifulSoup(res.text,'html.parser')
    linkElems = soup.select('.package-snippet')
    # print(linkElems[4].get('href'))
    for i in range(min(5,len(linkElems))) :
        urlToopen = 'https://pypi.org{}'.format(linkElems[i].get('href'))
        webbrowser.open(urlToopen)


search_pypi()