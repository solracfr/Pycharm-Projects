# import smtplib
#
# my_email = "solracfresh1@yahoo.com"
# password = "79591Sgh!?"
#
# their_email = "solracfresh2@yahoo.com"
#
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:  # works like a file
#     connection.starttls()  # transport layer security - encrypts and creates secure connection
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs=their_email,
#                         msg="Subject:Hello :)\n\nThis is the body of my email")

import datetime as dt  # less confusing this way
import random

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()  # 0 = Monday, 6 = Sunday

date = dt.datetime(year=2020, month=8, day=3)
print(now.strftime("%A"))  # strftime() returns day of week in name ("Monday")

with open("quotes.txt") as quotes_file:
    all_quotes = quotes_file.readlines()  # returns as list

    quote = random.choice(all_quotes)

    print(quote)


