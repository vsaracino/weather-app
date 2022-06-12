import requests

def getWeatherData(zip_code):
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?zip="+zip_code+",us&appid=4edfc63d0382435f01c9305149cf5e2b&units=imperial")
    return response.json()


if __name__ == "__main__":
  jsonResponse = getWeatherData()
  print(jsonResponse)