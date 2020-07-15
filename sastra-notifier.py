from bs4 import BeautifulSoup
import requests
import time
from notify_run import Notify
new_circular=[]
notify = Notify()
#x=notify.register()
#print(x)                

while True:
    url = "https://www.sastra.edu/"
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    
    response = requests.get(url,headers=headers)
    
    soup = BeautifulSoup(response.text, "lxml")

    container = soup.find('div', id = 'user6')

    rows = container.find_all('li')

    links = []
    
    for row in rows:
        link = row.find('a', href=True)
        links.append(url[:-1]+link['href'])

    new_links=list(set(links)-set(new_circular))

    for link in new_links:
        msg = "New circular(s) from SASTRA : " + link            
        notify.send(msg, link)
        print(link)         
            
    new_circular=links[:]
    time.sleep(3)        
            

