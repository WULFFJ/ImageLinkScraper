from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

inp = input("Enter page for Images:")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}
response = requests.get(inp, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
images = soup.find_all('img')

for item in images:
    print(item['src'])
