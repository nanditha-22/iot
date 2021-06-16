from flask import Flask
import pymysql
import requests,json

#Insert your OpenWeatherMap API here
OPEN_WEATHER_MAP_API_KEY = "cac6b559b0d76b60b320249526622c0a"

#give your Lattitude and Longitude
lat = '13.0878'
lon = '80.2785'

#Create openweathermap url
api_url = "https://api.openweathermap.org/data/2.5/onecall?lat="+str(lat)+"&lon="+str(lon)+"&exclude=hourly,daily,minutely,alerts+&appid="+OPEN_WEATHER_MAP_API_KEY+"&units=metric"

app = Flask(__name__)
@app.route('/fetchWeather')
def get_open_weather_map_data():
  
  response = requests.get(api_url).json()
  
  print(response)
  return response

 #To save API response to mySQL
@app.route('/todb')
def todb():
  
  #receiving data from OpenWeatherMap
 response = requests.get(api_url)
 if response.status_code == 200:
  data=response.json()
  #Cleaning the data to make it look tidy
  curr = data['current']
  clouds=curr['clouds']
  dew_point=curr['dew_point']
  dt=curr['dt']
  feels_like=curr['feels_like']
  humidity=curr['humidity']
  temp=curr['temp']
  
  report = curr['weather'][0]
  id=report['id'] 
  description=report['description']
  icon=report['icon'] 
  main=report['main'] 
  print("Current Weather:")
  print(f"clouds: {clouds}")
  print(f"dew_point: {dew_point}")
  print(f"dt: {dt}")
  print(f"feels_Like: {feels_like}") 
  print(f"Humidity: {humidity}")
  print(f"Temperature: {temp}")
  print("Weather Report")
  print(report)
  print(f"id: {id}")
  print(f"description: {description}")
  print(f"icon: {icon}")
  print(f"main: {main}") 
  
  else:
   # showing the error message
   print("Error in the HTTP request")
    
    #Configuring Connection to MYsql
 conn = pymysql.connect(database="db1",user="Sreenidhi",password="12345",host="localhost")
 cur=conn.cursor()
  
  #Table 1 shows realtime weather
 cur.execute("INSERT INTO currentWeatherTable VALUES (%s, %s, %s, %s, %s, %s)",(clouds,dew_point,dt,feels_like,humidity,temp))

 #Table 2 shows summary
 cur.execute("INSERT INTO weatherSummaryTable VALUES (%s, %s, %s, %s)",(id,description,icon,main))
 return curr

if __name__ == "__main__":
  #Application runs on port 3000
  app.run(host="0.0.0.0", port='3000', debug=1)
