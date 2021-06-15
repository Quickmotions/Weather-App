
#Python UI
from tkinter import *
#python image collection
from PIL import ImageTk, Image
#Web API interaction
import requests

class Weather:
    def __init__(self, master):
        #setup deafaults
        #default data set to london
        self.data = {'coord': {'lon': -0.1257, 'lat': 51.5085}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 'base': 'stations', 'main': {'temp': 296.91, 'feels_like': 296.73, 'temp_min': 294.12, 'temp_max': 298.3, 'pressure': 1022, 'humidity': 53}, 'visibility': 10000, 'wind': {'speed': 4.12, 'deg': 90}, 'clouds': {'all': 20}, 'dt': 1623762414, 'sys': {'type': 2, 'id': 2019646, 'country': 'GB', 'sunrise': 1623728567, 'sunset': 1623788360}, 'timezone': 3600, 'id': 2643743, 'name': 'London', 'cod': 200}
        #create all items for UI
        self.canvas = Canvas(master, bg="blue", height=450, width=450)
        self.background_label = Label(image=ImageTk.PhotoImage(Image.open("Images\\clear.jpg")))
        self.cityEntry = Entry()
        self.location = Label(text="City: " + self.data['name'], justify='center', anchor=CENTER, width=450)
        self.weatherDesc = Label(text="Weather: " + self.data["weather"][0]['description'], justify='center', anchor=CENTER, width=450)
        self.temperature = Label(text="Temperature: " + str(round(self.data["main"]['temp'] - 273, 1)) + "°C", justify='center', anchor=CENTER, width=450)
        self.windspeed = Label(text="Windspeed: " + str(round(self.data['wind']['speed'] * 1.15 * 2, 1)) + "mph", justify='center', anchor=CENTER, width=450)
    
    def getWeather(self, city):
        #ran every 2 secs
        #get api data from selected city
        api = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key['OpenWeatherMap']
        #ignore requests when input is missing or incorrect
        if(requests.get(api).json() != {'cod': '400', 'message': 'Nothing to geocode'} and requests.get(api).json() != {'cod': '404', 'message': 'city not found'}):
            self.data = requests.get(api).json()
            print(self.data["weather"][0]['main']) #testing
            #find correct image for weather type
            if self.data["weather"][0]['main'] == "Clear":
                img = ImageTk.PhotoImage(Image.open("Images\\clear.jpg"))
            elif self.data["weather"][0]['main'] == "Fog":
                img = ImageTk.PhotoImage(Image.open("Images\\fog.jpg"))
            elif self.data["weather"][0]['main'] == "Clouds":
                img = ImageTk.PhotoImage(Image.open("Images\\cloud.jpg"))
            elif self.data["weather"][0]['main'] == "Rain":
                img = ImageTk.PhotoImage(Image.open("Images\\rain.jpg"))
            elif self.data["weather"][0]['main'] == "Snow":
                img = ImageTk.PhotoImage(Image.open("Images\\snow.jpg"))
            else:
                img = ImageTk.PhotoImage(Image.open("Images\\storm.jpg"))
            #load image into background and anchor
            self.background_label.config(image=img)
            self.background_label.photo = img
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
            #setup all labels with weather details from location data
            self.location.config(text="City: " + self.data['name'], justify='center', anchor=CENTER, width=450)
            self.weatherDesc.config(text="Weather: " + self.data["weather"][0]['description'], justify='center', anchor=CENTER, width=450)
            self.temperature.config(text="Temperature: " + str(round(self.data["main"]['temp'] - 273, 1)) + "°C", justify='center', anchor=CENTER, width=450)
            self.windspeed.config(text="Windspeed: " + str(round(self.data['wind']['speed'] * 1.15 * 2, 1)) + "mph", justify='center', anchor=CENTER, width=450)
            #pack everything on the UI
            self.location.pack()
            self.weatherDesc.pack()
            self.temperature.pack()
            self.windspeed.pack()
            self.cityEntry.pack(pady=10)
            self.canvas.pack()
        #loop this check/update every 2000 millisecs
        root.after(2000, lambda: self.getWeather(self.cityEntry.get()))

#get API key
import json
with open('api_keys.py', 'r') as f:
    api_key = json.loads(f.read())

#create UI window
root = Tk()
root.title("Weather App")
root.geometry("450x450")
#initialise setup and set default location to London
classMaster = Weather(root)
classMaster.getWeather("London")
root.mainloop()
   
