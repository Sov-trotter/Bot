import requests
from dateutil.parser import parse
from bs4 import BeautifulSoup

def portfolio():
    url = "http://nith.ac.in/portfolios/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html5lib') 
    table = soup.find_all('ul', {"class":"dropdown-menu"})
    print("Enter \n 0) for architecture \n 1) for Centre For Energy & Environmental \n 2)for Material Science & Engineering \n  3) forChemical Engineering \n 4) Chemistry \n 5)Civil Engineering \n 6)Computer Science & Engineering \n 7)Electrical Engineering \n 8)Electronics & Communication Engineering /n 9)Humanities & Social Sciences  \n 10) Mathematics & Scientific Computing  \n 11)Mechanical Engineering  /n 12)Physics & Photonics Science  \n 13)Management Studies  \n ")
    t =int(input())

    for element in table:
      obj = {}
      tds = element.findAll('li')
      obj['link']=tds[t].contents[0]['href']
      return obj['link']
   
import requests
from dateutil.parser import parse
from bs4 import BeautifulSoup

def past_events():
    url = portfolio()
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html5lib') 
    past_event = []
    c=0
    table = soup.find_all('div' , {"id":"home"})
    f= table[0].find_all('table', {"class":"profilemain"})
    for table in f:
      c +=1
    print(c)
    for i in range(0,7):
      print("\n\n\n\n\n\n\n")
      table = soup.find_all('table', )[i].tbody.findAll('tr')
      for element in table :
         obj = {}
         tds=element.findAll('td')
         obj['title']=tds[0].text
         obj['name']=tds[2].text
         print(obj['title'])
         print(obj['name'])
