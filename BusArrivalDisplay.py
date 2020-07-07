# import all relevant libraries
import json
import math
import datetime
import requests
from tkinter import *
from PIL import ImageTk, Image
import httplib2 as http  # External library
from urllib.parse import urlparse

# Setup GUI
window = Tk()
window.title("Welcome to the Smart Bus Stop test")
window.configure(bg='black')

# Setup GUI Frames
timeWidget = LabelFrame(window, bg='steel blue', bd=0)
timeWidget.pack(side=TOP, fill=X)

frame = LabelFrame(window, bg='black', bd=0)
frame.pack(side=TOP, fill=X)


# Get current time and format it
def time():
    now = datetime.datetime.now()
    Time = now.strftime("%H:%M")
    Day = now.strftime("%A")
    Date = now.strftime("%b %d, %Y")
    # configure text in widget
    displayTime.configure(text=Time + "  ")
    displayDay.configure(text=Day + "  ")
    displayDate.configure(text=Date + "  ")
    window.after(1000, time)


# Display time
displayTime = Label(timeWidget, text='', font=("Helvetica", 50), bg="steel blue", fg="white")
displayTime.pack(side=LEFT)
displayDay = Label(timeWidget, text='', font=("Helvetica", 20), bg="steel blue", fg="white")
displayDay.pack(side=LEFT)
displayDate = Label(timeWidget, text='', font=("Helvetica", 20), bg="steel blue", fg="white")
displayDate.pack(side=LEFT)

# Get bus arrival time info
if __name__ == "__main__":
    # Authentication parameters
    headers = {'AccountKey': 'NXpFdS3XQnqaH4jIc2g6kQ==',
               'accept': 'application/json'}  # this is by default

    # API parameters
    uri = 'http://datamall2.mytransport.sg/'  # Resource URL
    path = 'ltaodataservice/BusArrivalv2?BusStopCode=75279'

# Build query string & specify type of API call
target = urlparse(uri + path)
print(target.geturl())
method = 'GET'
body = ''

# Get handle to http
h = http.Http()

# Obtain results
response, content = h.request(target.geturl(), method, body, headers)

# Parse JSON to print
jsonObj = json.loads(content)

z = len(jsonObj['Services'])

BusService = ['', '', '', '', '']
min1 = ['', '', '', '', '']
min2 = ['', '', '', '', '']
interchange = ['', '', '', '', '']
destination = ['', '', '', '', '']

# Set up bus arrival GUI
BusNo = Label(frame, text="   Bus   ", font=("Helvetica", 30), bg="pale green", fg="black")
BusNo.grid(row=0, column=0)
NextBus = Label(frame, text=" Due in (mins) ", font=("Helvetica", 30), bg="pale green", fg="black")
NextBus.grid(row=0, column=1)
SubBus = Label(frame, text=" Next (mins) ", font=("Helvetica", 30), bg="pale green", fg="black")
SubBus.grid(row=0, column=2)
terminal = Label(frame, text="                      Destination                      ", font=("Helvetica", 30),
                 bg="pale green", fg="black")
terminal.grid(row=0, column=3)


# Get bus arrival time info
def data():
    now = datetime.datetime.now()
    if __name__ == "__main__":
        # Authentication parameters
        headers = {'AccountKey': 'NXpFdS3XQnqaH4jIc2g6kQ==',
                   'accept': 'application/json'}  # this is by default

        # API parameters
        uri = 'http://datamall2.mytransport.sg/'  # Resource URL
        path = 'ltaodataservice/BusArrivalv2?BusStopCode=75279'

    # Build query string & specify type of API call
    target = urlparse(uri + path)
    method = 'GET'
    body = ''

    # Get handle to http
    h = http.Http()

    # Obtain results
    response, content = h.request(target.geturl(), method, body, headers)

    # Parse JSON to print
    jsonObj = json.loads(content)

    z = len(jsonObj['Services'])

    global BusService
    global min1
    global min2

    BusService = ['', '', '', '', '']
    firstBus = ['', '', '', '', '']
    secBus = ['', '', '', '', '']
    Bus1 = ['', '', '', '', '']
    Bus2 = ['', '', '', '', '']
    BusTiming1 = ['', '', '', '', '']
    BusTiming2 = ['', '', '', '', '']
    BusArr1 = ['', '', '', '', '']
    BusArr2 = ['', '', '', '', '']
    min1 = ['', '', '', '', '']
    min2 = ['', '', '', '', '']
    interchange = ['', '', '', '', '']
    destination = ['', '', '', '', '']

    # Clean the json data
    for x in range(z):
        BusService[x] = jsonObj['Services'][x]['ServiceNo']
        firstBus[x] = jsonObj['Services'][x]['NextBus']['EstimatedArrival']
        secBus[x] = jsonObj['Services'][x]['NextBus2']['EstimatedArrival']
        interchange[x] = jsonObj['Services'][x]['NextBus']['DestinationCode']

        if secBus[x] != '':
            Bus2[x] = (secBus[x].replace("T", " ")).replace("+08:00", "")
            BusTiming2[x] = datetime.datetime.strptime(Bus2[x], '%Y-%m-%d %H:%M:%S')
            BusArr2[x] = ((BusTiming2[x] - now).total_seconds()) / 60
            min2[x] = math.trunc(BusArr2[x])
            if min2[x] <= 1:
                min2[x] = "Arr"
        else:

            min2[x] = ""

        Bus1[x] = (firstBus[x].replace("T", " ")).replace("+08:00", "")
        BusTiming1[x] = datetime.datetime.strptime(Bus1[x], '%Y-%m-%d %H:%M:%S')
        BusArr1[x] = ((BusTiming1[x] - now).total_seconds()) / 60
        min1[x] = math.trunc(BusArr1[x])
        if min1[x] <= 1:
            min1[x] = "Arr"

        # Assign busstop code with their respective location
        if interchange[x] == '75009':
            interchange[x] = 'Tampines'
        elif interchange[x] == '84009':
            interchange[x] = 'Bedok'
        elif interchange[x] == '64009':
            interchange[x] = 'Hougang'
        elif interchange[x] == '76139':
            interchange[x] = 'Opp Century Square'

        print(BusService[x])
        print(min1[x])
        print(min2[x])
        print("\n")

    # Update bus arrival time
    for x in range(z):
        labels[x][0]['text'] = BusService[x]
        labels[x][1]['text'] = min1[x]
        labels[x][2]['text'] = min2[x]
        labels[x][3]['text'] = interchange[x]
    window.after(1000, data)  # Update labels after 1 seconds

# Display bus arrival time
labels = []
for x in range(z):
    ServiceNo = Label(frame, text=BusService[x], font=("Helvetica", 30), bg="black", fg="white")
    ServiceNo.grid(row=x + 1, column=0)
    Bus1 = Label(frame, text=min1[x], font=("Helvetica", 30), bg="black", fg="white")
    Bus1.grid(row=x + 1, column=1)
    Bus2 = Label(frame, text=min2[x], font=("Helvetica", 30), bg="black", fg="white")
    Bus2.grid(row=x + 1, column=2)
    destination = Label(frame, text=interchange[x], font=("Helvetica", 30), bg="black", fg="white")
    destination.grid(row=x + 1, column=3)
    labels.append([ServiceNo, Bus1, Bus2, destination])


# Get weather data
def getWeather():
    now = datetime.datetime.now()
    Hour = now.hour
    city = 'singapore'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=8bbaa9aac07b8b7aee5d54eee1e7cfdd&units=metric'.format(
        city)
    res = requests.get(url)
    data = res.json()
    global icon

    Code = data['weather'][0]['id']
    temp = data['main']['temp']
    description = data['weather'][0]['description']

    temp = round(temp, 1)  # round to 1 dp

    # Assign code with the respective icons
    if Code < 300:
        icon = ImageTk.PhotoImage(Image.open("11d@2x.png"))

    elif Code < 400:
        icon = ImageTk.PhotoImage(Image.open("09d@2x.png"))

    elif Code < 510 and (Hour <= 18 and Hour >= 7):
        icon = ImageTk.PhotoImage(Image.open("10d@2x.png"))

    elif Code < 510 and (Hour >= 19 and Hour <= 6):
        icon = ImageTk.PhotoImage(Image.open("10n@2x.png"))

    elif Code < 600:
        icon = ImageTk.PhotoImage(Image.open("09d@2x.png"))

    elif Code < 800:
        icon = ImageTk.PhotoImage(Image.open("50d@2x.png"))

    elif Code == 800 and (Hour <= 18 and Hour >= 7):
        icon = ImageTk.PhotoImage(Image.open("01d@2x.png"))

    elif Code == 800 and (Hour >= 19 and Hour <= 6):
        icon = ImageTk.PhotoImage(Image.open("01n@2x.png"))

    elif Code == 801 and (Hour <= 18 and Hour >= 7):
        icon = ImageTk.PhotoImage(Image.open("02d@2x.png"))

    elif Code == 801 and (Hour >= 19 and Hour <= 6):
        icon = ImageTk.PhotoImage(Image.open("02n@2x.png"))

    elif Code == 802 and (Hour <= 18 and Hour >= 7):
        icon = ImageTk.PhotoImage(Image.open("03d@2x.png"))

    elif Code == 802 and (Hour >= 19 and Hour <= 6):
        icon = ImageTk.PhotoImage(Image.open("03n@2x.png"))

    elif Code < 810:
        icon = ImageTk.PhotoImage(Image.open("04d@2x.png"))

    # Update weather data
    weather.config(image=icon)
    Temperature.config(text='{}°C'.format(temp))
    forecast.config(text=description + "  ")

    window.after(10000, getWeather)

# Set up weather GUI
weather = Label(timeWidget, image='', bg="steel blue")
Temperature = Label(timeWidget, text='', font=("Helvetica", 30), bg="steel blue", fg="white")
forecast = Label(timeWidget, text='', font=("Helvetica", 15), bg="steel blue", fg="white")

weather.pack(side=RIGHT)
Temperature.pack(side=RIGHT)
forecast.pack(side=RIGHT)

#run the functions
time()
getWeather()
data()

#Set GUI to fullscreen
window.attributes("-fullscreen", True)
#Press ESC to exit the program
window.bind("<Escape>", exit)
window.mainloop()
