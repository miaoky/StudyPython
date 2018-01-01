import requests
from bs4 import BeautifulSoup
import time

responseAns = requests.get("http://www.baidu.com")
responseAns.encoding = "utf-8"
html = responseAns.text
bs = BeautifulSoup(html, "lxml")
hrefs = bs.find_all("a")
for href in hrefs:
    print(href.get("href"))
    time.sleep(1)
