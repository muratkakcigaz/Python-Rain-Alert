import requests
import os
import dotenv

#For sending mail#
import smtplib


API_KEY=os.getenv('API_KEY')
EMAIL=os.getenv('EMAIL')
EMAIL_PASSWORD=os.getenv('EMAIL_PASSWORD')

def configure():
    dotenv.load_dotenv()

def send_mail(to, subject, body):
    with smtplib.SMTP(host="smtp@gmail.com",port=587,) as connection:
        connection.starttls()

        connection.login(user=EMAIL,password=EMAIL_PASSWORD)

        message= f"Subject:{subject}\n\n{body}"

        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=to,
            msg=message
        )

def will_it_rain(data):
    for x in range(0,4):
        if data["list"][x]["weather"][0]["id"]<700:
            print(data["list"][x]["weather"][0]["id"])
            will_rain=True
    if will_rain:
        send_mail(
            to="",
            subject="",
            body=""
        )




def main():
    configure()
    ENDPOINT="https://api.openweathermap.org/data/2.5/forecast"
    parameters={
        "lat":40.978796,
        "lon":28.719360,
        "appid":os.getenv(API_KEY),
        "cnt":4,#count of timestamps 3-6-9-12 #limiting timestamp to near future
    }
    response=requests.get(url=ENDPOINT,params=parameters)
    response.raise_for_status()
    print(response.status_code)
    data=response.json()
    print(data)
    will_it_rain(data=data)


main()