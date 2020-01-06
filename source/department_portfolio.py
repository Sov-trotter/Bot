import requests
from dateutil.parser import parse
from bs4 import BeautifulSoup

def portfolio():
    url = "http://nith.ac.in/portfolios/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html5lib') 
    table = soup.find_all('ul', {"class":"dropdown-menu"})
    print("Enter \n 0)Architecture\n 1)Centre For Energy & Environmental\n 2)Material Science & Engineering\n 3)Chemical Engineering\n 4)Chemistry\n 5)Civil Engineering\n 6)Computer Science & Engineering\n 7)Electrical Engineering\n 8)Electronics & Communication Engineering\n 9)Humanities & Social Sciences\n 10)Mathematics & Scientific Computing\n 11)Mechanical Engineering \n 12)Physics & Photonics Science\n 13)Management Studies\n ")
    t =int(input())

    for element in table:
      obj = {}
      tds = element.findAll('li')
      obj['link']=tds[t].contents[0]['href']
      return obj['link']
def department_portfolio():
    url = portfolio()
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html5lib') 
    portfolio_arr = []
    c=0
    table = soup.find_all('div' , {"id":"home"})
    f= table[0].find_all('table', {"class":"profilemain"})
    for table in f:
      c +=1
    for i in range(0,c):
      print("\n")
      table = soup.find_all('table', )[i].tbody.findAll('tr')
      for element in table :
         obj = {}
         tds=element.findAll('td')
         obj=tds[0].text +" : "+ tds[2].text 
        #  portfolio_arr.append()
         portfolio_arr.append(obj)
    return portfolio_arr
        
