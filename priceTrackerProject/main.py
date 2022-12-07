import lxml
import requests
from bs4 import BeautifulSoup
from smtplib import SMTP

KEYBOARD_URL = 'https://www.amazon.com/dp/B07WJZCPT3/ref=twister_B09NH8PG5W?_encoding=UTF8&th=1'
params = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-us',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'
}

response = requests.get(KEYBOARD_URL, headers=params)
print(response.text, response.status_code)

soup = BeautifulSoup(response.content, 'lxml')
print(soup.prettify())

product_title = soup.select_one(selector='#productTitle')
price = soup.select_one(selector='.a-price-whole')
fraction = soup.select_one(selector='.a-price-fraction')

print(f'{product_title.text}: {price.text}{fraction.text}')  # .text will only grab the immediate container, and not any children
