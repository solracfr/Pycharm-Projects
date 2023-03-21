import requests
from datetime import datetime
import smtplib

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour_now = time_now.hour

print(sunrise, sunset)
print(iss_longitude, iss_latitude)

if abs(iss_longitude-MY_LONG) <= 5 and abs(iss_latitude-MY_LAT) <= 5 and hour_now > sunset:
    with smtplib.SMTP("smtp.gmail.com", port=568) as smtp:
        smtp.starttls()
        smtp.login(user="solracfresno@gmail.com", password="password")
        smtp.send_message(msg="hi", from_addr="me", to_addrs="you")

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



