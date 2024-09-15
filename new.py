import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://www.telegraf.rs/'

# Send a request to the URL
response = requests.get(url)

# Parse the content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find elements (example: all <a> tags)
links = soup.find_all('a')

# Print the links
for link in links:
    print(link.get('href'))
