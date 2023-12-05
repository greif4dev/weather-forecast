import requests
from dataclasses import dataclass

API_KEY = "40fc25677a830026dc3505d99e37020d"

@dataclass
class WeatherData:
    descricao: str
    icon: str
    temp: int
    feels_like: int
    wind: int
    name: str

def getCity(cidadeUser):
    URL = f"https://pro.openweathermap.org/data/2.5/weather?q={cidadeUser}&lang=pt_br&APPID={API_KEY}&units=metric"
    response = requests.get(URL).json()
    data = WeatherData(
        descricao = response.get('weather')[0].get('description'),
        icon = response.get('weather')[0].get('icon'),
        temp = int(response.get('main').get('temp')),
        feels_like = int(response.get('main').get('feels_like')),
        wind = int(response.get('wind').get('speed')),
        name = "Neste momento em "+response.get('name')
    )
    return data

def main(cityUser):
    weather_data = getCity(cityUser)
    return weather_data

if __name__=="__main__":
    print(getCity('Florianópolis'))