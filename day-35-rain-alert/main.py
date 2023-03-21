#  failsafe code for Twilio recovery: 9IINREIYRe3IQAZDr66NXso_IHVgoR3EY2JcwtfZ
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import requests

#  use a proxy client server to send messages to
proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC699eda82af1a6cbd28e82e11116a301a"
auth_token = "c0543d1b7329fb506d6db20fab09cc9f"
api_key = os.environ.get("API_KEY")

parameters = {
    "lat": 35.4,  # ints are okay for url inputs
    "lon": -97.5,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
# print(response.text)
weather_data = response.json()  # return data in json format, but as a dict type
# print(type(weather_data["hourly"]))  # returns list
first_12_hrs = weather_data["hourly"][:12]  # return first 12 elements
# print(first_12_hrs[0]["weather"][0]["id"])  # returns the int for the weather code
first_12_weather_ids = [entry["weather"][0]["id"] for entry in first_12_hrs]  # returns the ints for all 12 hours
print(first_12_weather_ids)

will_rain = True in (item < 700 for item in first_12_weather_ids)  # generator comprehension

if will_rain:
    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages \
        .create(
        body="It's going to rain today, be sure to bring an umbrella",
        from_="+14142614515",
        to='+19567759902'
    )

    print(message.status)
