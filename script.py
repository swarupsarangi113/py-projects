import requests
from bs4 import BeautifulSoup
import string
import time
import pandas as pd
from multiprocessing.pool import ThreadPool

def all_branches(url):

    comp_id = url.split('/')[-1]
    data = {'comp_id': comp_id}

    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'method': 'POST',
    'origin': 'https://dcciinfo.ae',
    'referer': url,
    'x-requested-with': 'XMLHttpRequest'
    }

    cookies = {

    'cookie': '__cfduid=d0402551577d5fe6c45326fd4a8853bc91610384643; _ga=GA1.2.1649771966.1610384645; _gid=GA1.2.1364004218.1610947217; ci_session=85e8fc9de0a65b07cf682a92048a946c8a24fade; _gat=1'

    }

    r = requests.post('https://dcciinfo.ae/sitefront/clientcompanies/getBranchesBlockHtml', data=data, headers=headers,cookies = cookies)
    soup = BeautifulSoup(r.text, 'lxml')

    try :
        secondary_details = soup.find_all('div',class_='row p-2')
    except :
        pass

    data = {}
    json_data = []

    for detail in secondary_details :
        try :
            data['Phone'] = detail.find('div',class_='col-9 col-md-4').a['href'].split(':')[-1]
        except :
            data['Phone'] = ''
        try :
            data['Box'] = detail.find('div',itemprop='postOfceBoxNumber').text.strip()
        except :
            data['Box'] = ''
        try :
            data['Area'] = detail.find('div',class_='col-9 col-md-10').text.strip()
        except :
            data['Area'] = ''
        try :
            data['Address'] = detail.find('div',itemprop='addressRegion').text.strip()
        except :
            data['Address'] = ''
        try :
            data['Fax'] = detail.find_all('div',class_='col-9 col-md-4')[1].text.strip()
        except :
            data['Fax'] = ''
        try :
            data['City'] = detail.find('div',itemprop='addressLocality').text.strip()
        except :
            data['City'] = ''


        string = ''
        for key,value in data.items() :
            if value == '' :
                continue
            string += key +':'+ value +'\n'

        json_data.append(string)

    return '\n'.join(json_data)

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
            #branch_info = 'http://api.scrapestack.com/scrape?access_key={0}&url={1}'.format(token,company.find('strong').a['href'])
            r = requests.get(more_info_url).text
            obj = BeautifulSoup(r, 'html.parser')
            data['Catagory'] = catagory.text.strip()
            data['Company ID'] = more_info_url.split('/')[-1]
            name = company.find('strong').text.strip()
            data['Company Name'] = name
            print('Company Name', name)
            data['Keywords'] = ','.join([keyword.text for keyword in obj.find_all('a', class_='badge badge-pill badge-light font-14 clickKeys')])
            try :
                secondary_details = obj.find_all('div',class_='row p-2')
                secondary_details_1 = secondary_details[0]
                secondary_details_2 = secondary_details[1]
            except :
                pass
            try :
                data['Last Updated'] = secondary_details_1.find('div',class_='col-12').text.split(' - ')[-1]
            except :
                data['Last Updated'] = '' 
            try :
                data['Phone'] = secondary_details_1.find('div',class_='col-9 col-md-4').a['href'].split(':')[-1]
            except :
                data['Phone'] = ''
            try :
                data['Box'] = secondary_details_1.find('div',itemprop='postOfceBoxNumber').text.strip()
            except :
                data['Box'] = ''
            try :
                data['Area'] = secondary_details_1.find('div',class_='col-9 col-md-10').text.strip()
            except :
                data['Area'] = ''
            try :
                data['Website'] = secondary_details_1.find('a',class_='websiteClick').text.strip()
            except :
                data['Website'] = ''
            try :
                data['Address'] = secondary_details_1.find('div',itemprop='addressRegion').text.strip()
            except :
                data['Address'] = ''
            try :
                data['Fax'] = secondary_details_1.find_all('div',class_='col-9 col-md-4')[1].text.strip()
            except :
                data['Fax'] = ''
            try :
                data['City'] = secondary_details_1.find('div',itemprop='addressLocality').text.strip()
            except :
                data['City'] = ''
            try :
                data['Physical Location'] = secondary_details_2.find('a',class_='locationClicks')['href'].split('/')[-1]
            except :
                data['Physical Location'] = ''

            try :
                branch_details = all_branches(more_info_url)
                data['Branch Details'] = branch_details
            except :
                data['Branch Details'] = ''

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

        alphabets = ['A','B','C']

        with ThreadPool(3) as pool:
            pool.map(get_catagory_list, alphabets)


        print('******Job Details******')
        print('Total no of Companies scraped', len(json_data))

        # the json data is converted into a dataframe and saved into csv file
        df = pd.DataFrame(json_data)
        df.set_index('Company ID', inplace=True)
        df.to_excel('keyword_sheet.xlsx')
        print('Data saved into Excel file')

        print('Job Finished')

        finish = time.perf_counter()
        print(f'Finished in {round(finish-start, 2)} second(s)')

    except Exception as e:
        print(e)
        df = pd.DataFrame(json_data)
        df.set_index('Company ID', inplace=True)
        df.to_csv('keyword_sheet.csv')
