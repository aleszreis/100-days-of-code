import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os


OWM_ENDPOINT = "OPEN WEATHER MAP ENDPOINT"
api_key = "API KEY"
account_sid = "ACC SID"
auth_token = "AUTH TOKEN"

parameters = {
    "lat": -22.906847,
    "lon": -43.172897,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()

data = response.json()


data_slice = data["hourly"][:16]
will_rain = False
for hour in data_slice:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 600:
        will_rain = True
if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.environ["https_proxy"]}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="Vai chover hoje!",
        from_="+twilioPhoneNumber",
        to="+userPhoneNumber"
    )

    print(message.status)
