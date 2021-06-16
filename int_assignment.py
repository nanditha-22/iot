
import requests
#from flask import Flask
API_KEY = "7af490c1526a69f6b22bfded124ac80b"
city = "chennai"
api_url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_KEY
response = requests.get(api_url).json()
print(response)
for k,v in response.items():
    print(k,v)
import pymysql
City=response['name']
temperature=response['main']['temp']
latitude=response['coord']['lat']
longitude=response['coord']['lon']
feels_Like=response['main']['feels_like']
pressure=response['main']['pressure']
humidity=response['main']['humidity']
sea_level=response['main']['sea_level']
ground_level=response['main']['grnd_level']
wind_speed=response['wind']['speed']

data={'City':city,'Latitude':latitude,'Longitude':longitude,'Temperature':temperature,'WindSpeed':wind_speed,'FeelsLike':feels_Like,'Pressure':pressure,'Humidity':humidity,'SeaLevel':sea_level,'G>
print(data)
conn=pymysql.connect(database='Weather',user='Aparna',password='Appu123',host='localhost')
cur=conn.cursor()
cur.execute("INSERT INTO Weather_Data(City,Latitude,Longitude,Temperature,WindSpeed,FeelsLike,Pressure,Humidity,SeaLevel,GroundLevel) VALUES (%(City)s,%(Latitude)s,%(Longitude)s,%(Temperature)s,%>
conn.commit()
print('Saved to db')
