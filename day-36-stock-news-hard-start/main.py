import requests
from twilio.rest import Client
from datetime import date, timedelta

## ---------------------- SETUP VARIABLES --------------------- ##

SMS_ACCOUNT_SID = "AC699eda82af1a6cbd28e82e11116a301a"
SMS_AUTH_TOKEN = "c0543d1b7329fb506d6db20fab09cc9f"
TWILIO_PHONE_NUMBER = "+14142614515"
RECIPIENT_PHONE_NUMBER = "+19567759902"
client = Client(SMS_ACCOUNT_SID, SMS_AUTH_TOKEN)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "MGZKP0SP9ZXKU0B6"
NEWS_API_KEY = "2bad732df9ca4bec92142bf31c7b144a"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": STOCK_API_KEY
}

news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

## ---------------------- ACTUAL PROCESS --------------------- ##

#  get today, yesterday, and the day before yesterday, then convert the latter two to strings
today = date.today()
yesterday = str(today - timedelta(days=1))
day_before = str(today - timedelta(days=2))

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday.
# Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
stock_json = requests.get(url=STOCK_ENDPOINT, params=stock_parameters).json()  # get full query JSON
stock_time_series = stock_json["Time Series (Daily)"]  # get the time series section of info

#  get closing stocks for yesterday and the day before, and caluclate their absolute difference
# TODO: count only weekdays when referring to "yesterday" and "day before"
data_list = [value for (key, value) in stock_time_series.items()] # returns a list of tuples
closing_stock_yesterday = float(data_list[0]["4. close"])
closing_stock_day_before = float(data_list[1]["4. close"])

# closing_stock_yesterday = float(stock_time_series[yesterday]["4. close"])
# closing_stock_day_before = float(stock_time_series[day_before]["4. close"])
closing_difference = abs(closing_stock_yesterday - closing_stock_day_before)
print(closing_difference)
if closing_stock_yesterday - closing_stock_day_before > 0:
    triangle = "🔺"
else:
    triangle = "🔻"

#HINT 2: Work out the value of 5% of yerstday's closing stock price. 
percent = closing_difference / closing_stock_yesterday
print(percent)

# if percent > 0.05:
#     print("Get News")


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
if percent < 0.05:
    print("generating articles")
    news_json = requests.get(url=NEWS_ENDPOINT, params=news_parameters).json()
    news_json_first_three_articles = news_json["articles"][:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # Send a separate message with each article's title and description to your phone number.
    #HINT 1: Consider using a List Comprehension.

    #  content for articles in tuple form, which I hope is a good approach
    article_text_content = [(entry["title"], entry["content"]) for entry in news_json_first_three_articles]

    #  for each tuple, text the headline and article content
    for entry in article_text_content:
        message = client.messages.create(
            body=f"{STOCK}: {triangle} {int(percent * 100)}%\n\n"
                 f"Headline: {entry[0]}\n\n"
                 f"Brief: {entry[1]}",
            from_=TWILIO_PHONE_NUMBER,
            to=RECIPIENT_PHONE_NUMBER
        )

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

