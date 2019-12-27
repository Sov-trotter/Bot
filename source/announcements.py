import requests
from dateutil.parser import parse
from bs4 import BeautifulSoup

def announcements():
    url = "https://nith.ac.in"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html5lib') 
    announce = []
    table = soup.find_all('ul', {"style":"text-align:left; font-size: 20px"})#tbody.findAll('tr')   
    #table = soup.find_all('table', {"class":"dataTable"})[1].tbody.findAll('tr')
    i = 0
    announce =[]
    for element in table:{}
    for i in range(0,7):
            obj = {}
            tds = element.findAll('li')
            obj['Title'] = tds[i].contents[0].text
            obj['link'] = tds[i].contents[0]['href']
            i += 1
            announce.append(obj) 
    return announce
