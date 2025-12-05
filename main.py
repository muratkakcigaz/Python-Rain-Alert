import requests
import os
import dotenv

#For sending mail#
import smtplib



EMAIL=os.getenv('EMAIL')
EMAIL_APP_PASSWORD=os.getenv('EMAIL_PASSWORD')
HOST_FORMAT="smtp.live.com"
#smtp server adress
#Host Format can change depending on what you use
#ex for gmail accounts smptp.gmail.com



def configure():
    dotenv.load_dotenv()

def send_mail(to, subject, body):
    with smtplib.SMTP(host=HOST_FORMAT,port=587,timeout=60) as connection:
        connection.starttls()

        connection.login(user=EMAIL,password=EMAIL_APP_PASSWORD)

        message= f"Subject:{subject}\n\n{body}"

        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=to,
            msg=message
        )

def will_it_rain(data):
    will_rain=False
    for x in range(0,4):
        if data["list"][x]["weather"][0]["id"]<700:
            #print(data["list"][x]["weather"][0]["id"])
            will_rain=True
        if will_rain:
            send_mail(
                to="",
                subject="Rain Alert",
                body="There will be rain bring ambrella"
                )
        else:
            send_mail(
                to="",
                subject="Rain Alert",
                body="There will be no rain"
                )





def main():
    configure()
    ENDPOINT="https://api.openweathermap.org/data/2.5/forecast"
    parameters={
        "lat":41.247250,
        "lon":28.995118,
        "appid":os.getenv('API_KEY'),
        "cnt":4,#count of timestamps 3-6-9-12 #limiting timestamp to near future
    }
    response=requests.get(url=ENDPOINT,params=parameters)
    response.raise_for_status()
    print(response.status_code)
    data=response.json()
    print(data)
    will_it_rain(data)


main()
