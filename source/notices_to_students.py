import requests
from dateutil.parser import parse
from bs4 import BeautifulSoup

def notices_to_students():
    url = "http://nith.ac.in/?page_id=14888"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html5lib') 

    table = soup.find_all('table', {"align":"center"})#.tbody.find('tr') 
    table1 = table[0].find_all('tbody')
    table_fin = table1[0].find_all('tr')

    notice_students =[]
    for element in table_fin:
            obj = {}
            tds = (element.findAll('td'))#[0]#.findAll('div')
            tds_in = tds[0].findAll('b')
            obj['Title'] = tds_in[0].contents[0].text
            obj['link'] = tds_in[0].contents[0]['href']
            obj['Date of Upload'] = tds[3].contents[0]
            print(obj)
            notice_students.append(obj) 
    return notice_students
