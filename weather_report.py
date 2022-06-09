from flask import Flask, render_template, request
import weather_api

app = Flask(__name__)

@app.route('/')
def cond():
  print (request.args)
  zip_code = ''
  temperature = ''
  city = ''
  conditions = ''
  if len(request.args.getlist('zip')) > 0:
    zip_code = request.args['zip']
    temperature = str(weather_api.getTemp(zip_code))
    city = str(weather_api.getCity(zip_code))
    conditions = weather_api.getConditions(zip_code)
  return render_template ('weather.html.j2', zip=zip_code, tmp=temperature, city=city, conditions=conditions)

@app.route('/<zip>')
def hello(zip):
  print (request.args)
  return render_template ('weather.html.j2', zip=zip)

@app.route('/tmp')
def lat():
  return str(weather_api.getConditions('18702'))