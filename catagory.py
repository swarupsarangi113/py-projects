import requests
from bs4 import BeautifulSoup
import string
import time
import pandas as pd
import concurrent.futures
from multiprocessing.pool import ThreadPool

def get_companies_list(url):

    print('Getting Companies Info...')
    src = requests.get(url).text
    soup_obj = BeautifulSoup(src, 'html.parser')
    companies = soup_obj.find_all(
        'div', class_='col-sm-12 col-lg-6 p-0 p-lg-1')

    for i in range(2, 100):
        page_url = url + '/' + str((i - 1) * 30)
        page_src = requests.get(page_url).text
        page_soup = BeautifulSoup(page_src, 'html.parser')
        if page_soup == soup_obj:
            break
        else:
            companies.extend(page_soup.find_all(
                'div', class_='col-sm-12 col-lg-6 p-0 p-lg-1'))

    return companies


def get_catagory_list(letter):

    print('Looking into Catagories starting with letter ', letter)

    token = 'paste your scrapestack token here'
    url = 'https://dcciinfo.ae/categories/{}'.format(letter)
    # url = 'http://api.scrapestack.com/scrape?access_key={0}&url=https://dcciinfo.ae/categories/{1}'.format(token,letter)

    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')

    catagories = soup.find_all("div", class_='col-12 col-md-6 col-xl-4')

    # the below for loop is for the catagories which load once we scroll down the page
    for n in range(2, 15):
        src_load = requests.get(
            'https://dcciinfo.ae/loadmorecategories/{0}/{1}'.format(letter, n))
        soup_load = BeautifulSoup(src_load.text, 'html.parser')
        more_pages = soup_load.find_all(
            'div', class_='col-12 col-md-6 col-xl-4')
        if more_pages == []:
            break
        else:
            catagories.extend(more_pages)

    for catagory in catagories:
        catagory_url = catagory.a['href']
        # catagory_url = 'http://api.scrapestack.com/scrape?access_key={0}&url={1}'.format(token,catagory.a['href'])
        companies = get_companies_list(catagory_url)
        for company in companies:
            data = {}
            more_info_url = company.find('strong').a['href']
            # more_info_url = 'http://api.scrapestack.com/scrape?access_key={0}&url={1}'.format(token,company.find('strong').a['href'])
            r = requests.get(more_info_url).text
            obj = BeautifulSoup(r, 'html.parser')
            # data['Catagory'] = catagory.text.strip()
            data['Company ID'] = more_info_url.split('/')[-1]
            name = company.find('strong').text.strip()
            data['Company Name'] = name
            print('Company Name', name)
            data['Keywords'] = ','.join([keyword.text for keyword in obj.find_all(
                'a', class_='badge badge-pill badge-light font-14 clickKeys')])

            json_data.append(data)


if __name__ == '__main__':

    start = time.perf_counter()
    # json_data will contains all the information required by end user and in the end,save into a csv file
    json_data = []

    print('Job Started')
    print('Getting Catagories Info...')
    try:
        # alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
        #              'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        alphabets = ['J','Y','Z']
        # with concurrent.futures.ThreadPoolExecutor() as executor:
        #     executor.map(get_catagory_list, alphabets)

        with ThreadPool(3) as pool:
            pool.map(get_catagory_list, alphabets)

        print('******Job Details******')
        print('Total no of Companies scraped', len(json_data))

        # the json data is converted into a dataframe and saved into csv file
        df = pd.DataFrame(json_data)
        df.set_index('Company ID', inplace=True)
        df.to_csv('keyword_sheet.csv')
        print('Data saved into CSV file')

        print('Job Finished')

        finish = time.perf_counter()
        print(f'Finished in {round(finish-start, 2)} second(s)')

    except Exception as e:
        df = pd.DataFrame(json_data)
        df.set_index('Company ID', inplace=True)
        df.to_csv('keyword_sheet.csv')
