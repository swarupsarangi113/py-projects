import requests
from bs4 import BeautifulSoup
import string
import concurrent.futures
import time
import pandas as pd
from multiprocessing.pool import ThreadPool


def get_companies_list(url) :
    print('Getting Companies Info...')
    src = requests.get(url).text
    soup_obj = BeautifulSoup(src,'html.parser')
    companies = soup_obj.find_all('div',class_='col-12 col-lg-6 p-0 p-lg-1')
    
    for page in soup_obj.find_all('li',class_='page-item') :
        url = page.a['href']
        if url != '#' :
            src = requests.get(url).text
            soup_obj = BeautifulSoup(src,'html.parser')
            companies.extend(soup_obj.find_all('div',class_='col-12 col-lg-6 p-0 p-lg-1'))
    
    return companies

def get_catagory_list(letter) :
    print(letter)
    
    # token = ''

    url = 'https://dcciinfo.ae/categories/{}'.format(letter)
    #url = 'http://api.scrapestack.com/scrape?access_key={0}&url=https://dcciinfo.ae/categories/{1}'.format(token,letter)
    
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    
    catagories = soup.find_all("div",class_='col-12 col-md-6 col-xl-4')
    
    for catagory in catagories :
        catagory_url = catagory.a['href']
        #catagory_url = 'http://api.scrapestack.com/scrape?access_key={0}&url={1}'.format(token,catagory.a['href'])
        companies = get_companies_list(catagory_url)
        for company in companies :
            data = {}
            more_info_url = company.find('strong').a['href']
            #more_info_url = 'http://api.scrapestack.com/scrape?access_key={0}&url={1}'.format(token,company.find('strong').a['href'])
            r = requests.get(more_info_url).text
            obj = BeautifulSoup(r,'html.parser')
            data['Catagory'] = catagory.text.strip()
            data['Company ID'] = more_info_url.split('/')[-1]
            name = company.find('strong').text.strip()
            data['Company Name'] = name
            print('Company Name',name)
            #data['Keywords'] = ','.join([keyword.text for keyword in obj.find_all('a',class_='badge badge-pill badge-light font-14 clickKeys')])
            
            json_data.append(data)

if __name__ == '__main__' :
    
    start = time.perf_counter()
    json_data = []

    print('Job Started')
    print('Getting Catagories Info...')

    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     executor.map(get_catagory_list, alphabets)

    with ThreadPool(26) as pool:
        pool.map(get_catagory_list, alphabets)

    
    print('Total no of Companies scraped',len(json_data))
    
    df = pd.DataFrame(json_data)
    df.set_index('Company ID', inplace=True)
    df.to_csv('catagory.csv')
    
    print('Data saved into CSV file')
    print('Job Finished')

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')

