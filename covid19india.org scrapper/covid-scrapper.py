from bs4 import BeautifulSoup
import requests
import sys
import csv

url = 'https://api.covid19india.org/state_district_wise.json'

source = requests.get(url).text

soup = BeautifulSoup(source, 'lxml')

# extracting the data from the html tags
data = soup.html.body.p.text

# converting the string representation of dictionary to python dictionary
dict_data = eval(str(data))


state_name = input('Enter the name of state (Hint- Odisha) : ')

state_data = dict_data.get(state_name)


if state_data:
    districts_data = state_data['districtData']
else:
    print('State not Found, Please try again!')
    sys.exit()

# get multiple districts as a list from the user (Ex-Sambalpur,Khordha,Puri)
districts = input(
    'Enter the districts you want to know the data for(Ex:-Sambalpur,Angul,Puri) : ').split(',')


csv_file = open('covid19_scrap.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(
    ['State Name', 'District', 'New Cases', 'Active', 'Confirmed', 'Recovered', 'Deceased', 'Notes'])

for d in districts:
    status = districts_data.get(d)

    if status:
        notes = active = districts_data[d]['notes']
        new_cases = districts_data[d]['delta']['confirmed']

        active = districts_data[d]['active']
        confirmed = districts_data[d]['confirmed']
        recovered = districts_data[d]['recovered']
        deceased = districts_data[d]['deceased']

        csv_writer.writerow(
            [state_name, d, new_cases, active, confirmed, recovered, deceased, notes])
        print('Data written into CSV file...')

    else:
        print(f"district {d} not found.")

csv_file.close()
