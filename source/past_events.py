import requests
from dateutil.parser import parse
from bs4 import BeautifulSoup

def past_events():
    url = "http://nith.ac.in/?page_id=23481"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html5lib') 
    past_event = []
    table = soup.find_all('table', {"width":"100%"})[1].tbody.findAll('tr') #meta property="og:description"
    for element in table:
        obj = {}
        tds = (element.findAll('td'))
        obj['Title'] = tds[0].text
        obj['Date of Event'] = tds[1].text
        obj['Brochure link'] = "https://nith.ac.in" + tds[2].contents[0]['href']
        past_event.append(obj)
    return(past_event)
    