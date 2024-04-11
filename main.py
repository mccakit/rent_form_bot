from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import lxml
import requests
import time
firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=firefox_options)

my_header = {
    "Accept-Language":"tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
}
rent_site = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(url=rent_site,headers = my_header)
soup = BeautifulSoup(response.text,"lxml")

adress = soup.findAll(name="address")
adress = [n.text.strip() for n in adress]
rent_rate = soup.findAll(name="span",class_="PropertyCardWrapper__StyledPriceLine")
rent_rate = [n.text.strip() for n in rent_rate]
link = soup.findAll(name="a",class_="StyledPropertyCardDataArea-anchor")
link = [n.text.strip() for n in link]

driver.get("https://forms.gle/sjeEesprfuJqRmet5")
for n in range(len(adress)):
    questions = driver.find_elements(By.CLASS_NAME,value="whsOnd.zHQkBf")
    questions[0].send_keys(adress[n])
    questions[1].send_keys(rent_rate[n])
    questions[2].send_keys(link[n])
    time.sleep(2)

    send = driver.find_element(By.CLASS_NAME,value="NPEfkd.RveJvd.snByac")
    send.click()
    time.sleep(2)

    refresh = driver.find_element(By.TAG_NAME,value="a")
    refresh.click()
    time.sleep(2)
driver.quit()


