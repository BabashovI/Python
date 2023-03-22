import requests
from bs4 import BeautifulSoup

# Enter the tracking number to search
tracking_number = input("Enter the tracking number: ")

# URL to send the request
url = f"https://parcelsapp.com/en/tracking/{tracking_number}"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the response
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the tracking details
table = soup.find('table', {'class': 'tracking-table'})

# Extract the rows of the table
rows = table.find_all('tr')

# Extract the tracking details from each row
for row in rows:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    print('\t'.join(cols))
