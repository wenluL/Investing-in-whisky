import requests
from bs4 import BeautifulSoup
import urllib
import ssl
from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np
ssl._create_default_https_context = ssl._create_unverified_context

# All elements can be crawled using selenium
urls = "https://whiskyauction.com/wac/auctionBrowser"
driver = webdriver.Safari()
driver.get(urls)
links=driver.find_elements(By.CLASS_NAME, 'card-link')
l=[]
for link in links:
    ll = link.get_attribute("href")
    l.append(ll)
ll=np.unique(l)
number=0
for link in ll:
    url = link
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    params = {"show_ram": 1}
    response = requests.get(url, params=params, headers=headers)
    listData = []
    soup = BeautifulSoup(response.text, 'html.parser')
    tr = soup.find('table', class_='table detailpage-detaildata').find_all('tr')
    for j in tr[0:]:
        td = j.find_all('td')
        data = td[1].get_text().strip()
        listData.append(data)
    print(listData)
    number = number +1
print(number)
driver.quit()
