from cgitb import reset
import requests

def getTemp(zip_code):
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?zip="+zip_code+",us&appid=4edfc63d0382435f01c9305149cf5e2b&units=imperial")
    temperature = response.json()['main']['temp']
    return temperature

def getCity(zip_code):
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?zip="+zip_code+",us&appid=4edfc63d0382435f01c9305149cf5e2b&units=imperial")
    city = response.json()['name']
    return city

def getConditions(zip_code):
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?zip="+zip_code+",us&appid=4edfc63d0382435f01c9305149cf5e2b&units=imperial")
    condRef = response.json()['weather'][0]['description']
    condition = ""
    if condRef == 'clear sky':
      condition = 'clear skies'
    elif condRef == 'few clouds':
      condition = 'a few clouds'
    elif condRef == 'scattered clouds':
      condition = 'some scattered clouds'
    elif condRef == 'broken clouds':
      condition = 'broken clouds'
    elif condRef == 'shower rain':
      condition = 'rain showers'
    elif condRef == 'rain':
      condition = 'steady rain'
    elif condRef == 'thunderstorm':
      condition = 'thunderstoms'
    elif condRef == 'snow':
      condition = 'snow'
    elif condRef == 'mist':
      condition = 'misty skies'

    return condition


if __name__ == "__main__":
  jsonResponse = getConditions()
  print(jsonResponse)