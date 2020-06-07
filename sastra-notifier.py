from bs4 import BeautifulSoup
import requests
import time
#from email.mime.text import MIMEText
#import smtplib
from notify_run import Notify
new_circular=[]
notify = Notify()
x=notify.register()
print(x)                
#def Sastra_notifier(new_circular):
while True:
    url = "https://www.sastra.edu/"
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    
    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.text, "lxml")

    container = soup.find('div', class_='custom')

    rows = container.find_all('p')
    links = []
    for row in rows:
        if row.find('img'):
            link = row.find('a', href=True)
            links.append(link)
    #print(links)
        
    if links == new_circular:
        time.sleep(5)
        #Sastra_notifier(new_circular)

    else:
        new_circular = links
        count = len(links)
        for link in links:
            msg = str(count) + "new circular(s) from SASTRA : " + link.text            
            notify.send(msg, link['href'])
            print(link['href'])
            time.sleep(5)
            #Sastra_notifier(new_circular)
            
            
#Sastra_notifier(new_circular)
