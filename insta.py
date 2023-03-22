import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from requests_ntlm import HttpNtlmAuth
import datetime
import smtplib,pymongo
import pandas as pd
from openpyxl.workbook import Workbook
import json
url = 'https://www.instagram.com/makeup_stilist_aynur/followers/'
username, password = 'makeup_stilist_aynur', '0502133825'
response = requests.get(url, auth=HttpNtlmAuth(username, password))
m = response.search(r'"followed_by":\{"count":([0-9]+)\}', str(r.content))
print(m.group(1))
soup = BeautifulSoup(response.text, 'lxml')
all_data = soup.find_all("div")
#data = all_data[-1].find_all("td")
#print(all_data)