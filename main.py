
import requests
from dateutil.parser import parse
from bs4 import BeautifulSoup

def portfolio():
    url = "https://nith.ac.in"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html5lib') 
    t= input("enter the department  :")
    table = soup.find_all('ul', {"style":"dropdown-menu})
    for element in table:{}
    
            obj = {}
            tds = element.findAll('li')
              obj['Title'] = tds[i].contents[0].text
            
            obj['link'] = tds[0].contents[0]['href']
            if obj['Title']=t
            print(obj['link'])
    return portfolio 
