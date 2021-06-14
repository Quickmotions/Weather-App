import requests
def getWeather(city):
    api = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=ba20c35910ea8cfa41785d81baafa2c9"
    data = requests.get(api).json()
    print(data)
    print(data['wind']['speed'])
    return data
city = input("enter city name: ")
city = city[0].upper() + city[1:].lower()
data = getWeather(city)

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
lblwidth = 600
root.geometry("{}x450".format(lblwidth))

C = Canvas(root, bg="blue", height=250, width=300)


if data["weather"][0]['main'] == "Clear":
    img = ImageTk.PhotoImage(Image.open("Images\\clear.jpg"))
elif data["weather"][0]['main'] == "Clouds":
    img = ImageTk.PhotoImage(Image.open("Images\\cloud.jpg"))
elif data["weather"][0]['main'] == "Rain":
    img = ImageTk.PhotoImage(Image.open("Images\\rain.jpg"))
elif data["weather"][0]['main'] == "Snow":
    img = ImageTk.PhotoImage(Image.open("Images\\snow.jpg"))
else:
    img = ImageTk.PhotoImage(Image.open("Images\\storm.jpg"))

background_label = Label(root, image=img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

location = Label(text="City: " + data['name'], justify='center', anchor=CENTER, width=lblwidth)
weatherDesc = Label(text="Weather: " + data["weather"][0]['description'], justify='center', anchor=CENTER, width=lblwidth)
temperature = Label(text="Temperature: " + str(round(data["main"]['temp'] - 273, 1)) + "°C", justify='center', anchor=CENTER, width=lblwidth)
windspeed = Label(text="Windspeed: " + str(round(data['wind']['speed'] * 1.15 * 2, 1)) + "mph", justify='center', anchor=CENTER, width=lblwidth)


location.pack()
weatherDesc.pack()
temperature.pack()
windspeed.pack()

C.pack()
mainloop()
