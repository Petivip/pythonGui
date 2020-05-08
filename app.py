import tkinter as tk
import requests


def get_weather(city):
    weather_key = '958258f9b352314c08308cb3d849fb35'
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    respo = requests.get(url, params=params)

    label['text']=respo.json()['main']['temp']


root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=700)
canvas.pack()

background_image = tk.PhotoImage(file="")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='silver')
frame.place(relx=0.1, rely=0.1, relwidth=0.7, relheight=0.7)

button = tk.Button(frame, text="Search", bg='gray', fg='red', font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.6, rely=0.1, relwidth=0.3, relheight=0.1)

entry = tk.Entry(frame, font=40)
entry.place(relx=0.1, rely=0.1, relwidth=0.4, relheight=0.1)

lower_frame = tk.Frame(root, bg='black', bd=10)
lower_frame.place(relx=0.46, rely=0.27, relwidth=0.58, relheight=0.5, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()
