import requests
#from flask import Flask
API_KEY = "7af490c1526a69f6b22bfded124ac80b"
city = "chennai"
api_url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_KEY
response = requests.get(api_url).json()
print(response)
for k,v in response.items():
    print(k,v)
