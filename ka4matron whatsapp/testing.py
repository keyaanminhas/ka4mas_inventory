import requests

from bs4 import BeautifulSoup
from time import sleep



website = requests.get('https://www.goodreads.com/quotes/tag/unrequited-love')
soup = BeautifulSoup(website.content, 'html.parser')
my_classes = soup.find_all(class_ = 'quoteText')
for i in my_classes:
    print(i.text)