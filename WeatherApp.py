import requests
def getWeather(city):
    api = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=ba20c35910ea8cfa41785d81baafa2c9"
    data = requests.get(api).json()
    print(data["weather"][0]['description'])
    print(data)
    return data
    
data = getWeather("Glasgow")

from tkinter import *
from PIL import ImageTk, Image
root = Tk()

C = Canvas(root, bg="blue", height=250, width=300)


if data["weather"][0]['main'] == "Clear":
    img = ImageTk.PhotoImage(Image.open("Images\clear.jpg"))
elif data["weather"][0]['main'] == "Clouds":
    img = ImageTk.PhotoImage(Image.open("Images\cloud.jpg"))
else:
    img = ImageTk.PhotoImage(Image.open("Images\storm.jpg"))

background_label = Label(root, image=img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

weatherDesc = Label(text=data["weather"][0]['description'])
weatherDesc.pack()



C.pack()
mainloop()
