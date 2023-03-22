import requests
from bs4 import BeautifulSoup

url = 'https://day.az/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

headlines = [h2.text for h2 in soup.find_all('h2')]

print(headlines)
