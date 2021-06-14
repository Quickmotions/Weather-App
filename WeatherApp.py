import requests
def getWeather(city):
    api = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=ba20c35910ea8cfa41785d81baafa2c9"
    data = requests.get(api).json()
    print(data["weather"][0]['description'])
    print(data)
    
getWeather("Glasgow")

from tkinter import *
from tkinter import messagebox
top = Tk()

C = Canvas(top, bg="blue", height=250, width=300)
filename = PhotoImage(file = "Images/Cloudy.jpg")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()
top.mainloop