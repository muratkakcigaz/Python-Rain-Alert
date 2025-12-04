import requests
import os
import dotenv

def configure():
    dotenv.load_dotenv()



def main():
    configure()
    ENDPOINT="https://api.openweathermap.org/data/2.5/forecast"
    parameters={
        "lat":40.978796,
        "lon":28.719360,
        "appid":os.getenv('API_KEY'),
        "cnt":4,#count of timestamps 3-6-9-12 #limiting timestamp to near future
    }
    response=requests.get(url=ENDPOINT,params=parameters)
    response.raise_for_status()
    print(response.status_code)
    data=response.json()
    print(data)

main()