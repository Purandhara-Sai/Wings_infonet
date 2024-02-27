# The requests module in Python is commonly used for making HTTP requests to web servers..
import requests
from bs4 import BeautifulSoup

url = "https://www.magicbricks.com/"
response = requests.get(url)
print(response.status_code)

soup = BeautifulSoup(response.content,"html.parser")

print(soup)