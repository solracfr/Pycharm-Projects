import requests
from datetime import datetime
MY_LAT = 47.606209
MY_LNG = -122.332069

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()["iss_position"]  # returns a json that acts like a dictionary
# longitude = data["longitude"]
# latitude = data["latitude"]
#
# iss_position = (longitude, latitude)
#
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0  # shows UTC 24hr clock times
}

response = requests.get(url="http://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunrise = sunrise.split("T")[1].split(":")[0]
sunset = data["results"]["sunset"]
sunset = sunset.split("T")[1].split(":")[0]

now = datetime.now().hour

print(f"sunrise: {sunrise}\nsunset: {sunset}\nnow: {now}")
