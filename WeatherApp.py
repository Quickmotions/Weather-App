import requests
def getWeather(city):
    api = "api.openweathermap.org/data/2.5/weather?q="+city+"&appid=ba20c35910ea8cfa41785d81baafa2c9"
    data = requests.get(api).json()
    print(data)
    print()
    print(requests.get(api))
getWeather("Glasgow")