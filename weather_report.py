from flask import Flask, render_template, request
import weather_api

app = Flask(__name__)

@app.route('/')
def cond():
  print (request.args)
  weatherData = ''
  zip_code = ''
  temperature = ''
  city = ''
  condRef = ''
  condition = ''
  condImg = ''
  minTemp = ''
  maxTemp = ''
  windSpd = ''
  humidity = ''
  hexCode = ''

  if len(request.args.getlist('zip')) > 0:

    #assign zip code input to variable
    zip_code = request.args['zip']

    #API request and assign datapoints
    weatherData = weather_api.getWeatherData(zip_code)
    temperature = weatherData['main']['temp']
    city = weatherData['name']
    minTemp = weatherData['main']['temp_min']
    maxTemp = weatherData['main']['temp_max']
    humidity = weatherData['main']['humidity']
    windSpd = weatherData['wind']['speed']
  
    #test for conditions and display appropriate image
    condRef = weatherData['weather'][0]['main']
    if condRef == 'Clear':
      condition = 'clear skies'
      condImg = 'https://images.unsplash.com/photo-1506587767820-2718236a68fc?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80'
    elif condRef == 'Clouds':
      condition = 'a few clouds'
      condImg = 'https://images.unsplash.com/photo-1613539423218-6789cfcc5468?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80'
    elif condRef == 'Drizzle':
      condition = 'rain showers'
      condImg = 'https://images.unsplash.com/photo-1572455857811-045fb4255b5d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8ODN8fHJhaW55fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=400&q=60'
    elif condRef == 'Rain':
      condition = 'steady rain'
      condImg = 'https://images.unsplash.com/photo-1508081317905-6dd972f752dd?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80'
    elif condRef == 'Thunderstorm':
      condition = 'thunderstorms'
      condImg = 'https://images.unsplash.com/photo-1605727216801-e27ce1d0cc28?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8dGh1bmRlcnN0b3JtfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=400&q=60'
    elif condRef == 'Snow':
      condition = 'snow'
      condImg = 'https://images.unsplash.com/photo-1547754980-3df97fed72a8?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80'
    elif condRef == 'mist':
      condition = 'misty skies'
      condImg = 'https://images.unsplash.com/photo-1535165478661-5f1ff27a061b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2349&q=80'
    else:
      condImg = 'https://images.unsplash.com/photo-1506587767820-2718236a68fc?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80'

    #test for temp ranges and change text color based on that
    if temperature <= 32:
      hexCode = '0c43f7'
    elif temperature > 32 and temperature <=48:
      hexCode = '373ebf'
    elif temperature > 48 and temperature <=64:
      hexCode = '9296de'
    elif temperature > 65 and temperature <=75:
      hexCode = 'F8EB25'
    elif temperature > 75 and temperature <= 90:
      hexCode = 'a6791f'
    elif temperature > 90:
      hexCode = 'c4331a'

  #HTML render
  return render_template ('weather.html.j2', zip=zip_code, tmp=temperature, city=city, conditions=condition, cond_img=condImg, minTemp=minTemp, maxTemp=maxTemp, humidity=humidity, windSpd=windSpd, hexCode=hexCode)

#test routes
@app.route('/<zip>')
def hello(zip):
  print (request.args)
  return render_template ('weather.html.j2', zip=zip)

@app.route('/tmp')
def lat():
  return str(weather_api.getConditions('18702'))