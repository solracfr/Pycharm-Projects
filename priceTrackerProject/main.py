import lxml
import os
import requests
from bs4 import BeautifulSoup
from smtplib import SMTP,SMTP_SSL, SMTPException

# --------------------------------------------------SOUP PORTION----------------------------------------------------- #
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

# .text will only grab the immediate container, and not any children
print(f'{product_title.text}: {price.text}{fraction.text}')

# --------------------------------------------------EMAIL PORTION----------------------------------------------------- #

sender = 'solracfresno@gmail.com'
password = os.environ.get("EMAIL_PASSWORD")
receivers = ['solracfresno@gmail.com']

message = f"""From: From Person <{sender}>
To: To Person <{receivers[0]}>
Subject: Deal alert!

Good news! You've got a deal now:
Name: {product_title.text.strip()} 

Price: {price.text}{fraction.text}

URL: {KEYBOARD_URL}
"""
message = message.encode(encoding="utf-8")

try:
    server = SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user=sender, password=password)
    server.sendmail(from_addr=sender, to_addrs=receivers, msg=message)
    print('email successfully sent!')
except SMTPException:
    print('failed to send email')
