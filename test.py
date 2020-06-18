import json
import datetime
import requests
from tkinter import *
from PIL import ImageTk,Image
import httplib2 as http  # External library
from urllib.parse import urlparse

window = Tk()
window.title("Welcome to the Smart Bus Stop test")
window.configure(bg='black')

frame = LabelFrame(window,bg='black',bd = 0)
frame.pack(anchor = NW, side = LEFT)

timeWidget = LabelFrame(window, bg ='black', bd =0)
timeWidget.pack(anchor = NE, side = RIGHT)

weatherWidget = LabelFrame(window,bg='black', bd =0)
weatherWidget.pack(anchor = N, side = TOP)

#Displaying time
def time():

    now = datetime.datetime.now()
    Time = now.strftime("%H:%M")
    Day = now.strftime("%A")
    Date = now.strftime("%b %d, %Y")
    # configure text in widget
    displayTime.configure(text=Time)
    displayDay.configure(text=Day)
    displayDate.configure(text=Date)
    window.after(1000, time)


# Firstly create and pack widgets outside function:
displayTime = Label(timeWidget, text='', font=("Helvetica", 50), bg="black", fg="white")
displayTime.pack(anchor=E, side=TOP)
displayDay = Label(timeWidget, text='', font=("Helvetica", 15), bg="black", fg="white")
displayDay.pack(anchor=E, side=TOP)
displayDate = Label(timeWidget, text='', font=("Helvetica", 15), bg="black", fg="white")
displayDate.pack(anchor=E, side=TOP)

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
firstBus = ['', '', '', '', '']
secBus = ['', '', '', '', '']
Bus1 = ['', '', '', '', '']
Bus2 = ['', '', '', '', '']
BusTiming1 = ['', '', '', '', '']
BusTiming2 = ['', '', '', '', '']
BusArr1 = ['', '', '', '', '']
BusArr2 = ['', '', '', '', '']
hrMinSec1 = ['', '', '', '', '']
hrMinSec2 = ['', '', '', '', '']
MinSec1 = ['', '', '', '', '']
MinSec2 = ['', '', '', '', '']

for x in range(z):
    BusService[x] = jsonObj['Services'][x]['ServiceNo']
    firstBus[x] = jsonObj['Services'][x]['NextBus']['EstimatedArrival']
    secBus[x] = jsonObj['Services'][x]['NextBus2']['EstimatedArrival']

    Bus1[x] = firstBus[x].split('T')
    BusTiming1[x] = Bus1[x][1].split('+')
    BusArr1[x] = BusTiming1[x][0]
    hrMinSec1[x] = BusTiming1[x][0].split(':')
    MinSec1[x] = hrMinSec1[x][0] + ':' + hrMinSec1[x][1]

    if secBus[x] != '':
        Bus2[x] = secBus[x].split('T')
        BusTiming2[x] = Bus2[x][1].split('+')
        BusArr2[x] = BusTiming2[x][0]
        hrMinSec2[x] = BusTiming2[x][0].split(':')
        MinSec2[x] = hrMinSec2[x][0] + ':' + hrMinSec2[x][1]

    else:

        BusArr2[x] = secBus[x]

    print(BusService[x])
    print(MinSec1[x])
    print(MinSec2[x])


BusNo = Label(frame, text="   Bus   ", font=("Helvetica", 30), bg="black", fg="white")
BusNo.grid(row=0, column=0)
NextBus = Label(frame, text=" Next Bus ", font=("Helvetica", 30), bg="black", fg="white")
NextBus.grid(row=0, column=1)
SubBus = Label(frame, text=" Subsequent Bus ", font=("Helvetica", 30), bg="black", fg="white")
SubBus.grid(row=0, column=2)

labels = []
for x in range(z):

    ServiceNo = Label(frame, text=BusService[x], font=("Helvetica", 30), bg="black", fg="white")
    ServiceNo.grid(row=x + 1, column=0)
    Bus1 = Label(frame, text=MinSec1[x], font=("Helvetica", 30), bg="black", fg="white")
    Bus1.grid(row=x + 1, column=1)
    Bus2 = Label(frame, text=MinSec2[x], font=("Helvetica", 30), bg="black", fg="white")
    Bus2.grid(row=x + 1, column=2)
    labels.append([ServiceNo, Bus1, Bus2])


def data():
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

    BusService = ['', '', '', '', '']
    firstBus = ['', '', '', '', '']
    secBus = ['', '', '', '', '']
    Bus1 = ['', '', '', '', '']
    Bus2 = ['', '', '', '', '']
    BusTiming1 = ['', '', '', '', '']
    BusTiming2 = ['', '', '', '', '']
    BusArr1 = ['', '', '', '', '']
    BusArr2 = ['', '', '', '', '']
    hrMinSec1 = ['', '', '', '', '']
    hrMinSec2 = ['', '', '', '', '']
    MinSec1 = ['', '', '', '', '']
    MinSec2 = ['', '', '', '', '']

    for x in range(z):
        BusService[x] = jsonObj['Services'][x]['ServiceNo']
        firstBus[x] = jsonObj['Services'][x]['NextBus']['EstimatedArrival']
        secBus[x] = jsonObj['Services'][x]['NextBus2']['EstimatedArrival']

        Bus1[x] = firstBus[x].split('T')
        BusTiming1[x] = Bus1[x][1].split('+')
        BusArr1[x] = BusTiming1[x][0]
        hrMinSec1[x] = BusTiming1[x][0].split(':')
        MinSec1[x] = hrMinSec1[x][0] + ':' + hrMinSec1[x][1]

        if secBus[x] != '':
            Bus2[x] = secBus[x].split('T')
            BusTiming2[x] = Bus2[x][1].split('+')
            BusArr2[x] = BusTiming2[x][0]
            hrMinSec2[x] = BusTiming2[x][0].split(':')
            MinSec2[x] = hrMinSec2[x][0] + ':' + hrMinSec2[x][1]

        else:

            BusArr2[x] = secBus[x]

    for x in range(z):
        labels[x][0]['text'] = BusService[x]
        labels[x][1]['text'] = MinSec1[x]
        labels[x][2]['text'] = MinSec2[x]
    window.after(1000, data)  # Update labels after 1 seconds




#Displaying weather
def getWeather():

    now = datetime.datetime.now()
    Hour = now.hour
    city = 'singapore'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=12f6d11fed338d355ff4c13d4be587fa&units=metric'.format(city)
    res = requests.get(url)
    data = res.json()
    global icon

    Code = data['weather'][0]['id']
    temp = data['main']['temp']
    description = data['weather'][0]['description']

    temp = round(temp,1)    #round to 1 dp


    if Code < 300:
        icon = ImageTk.PhotoImage(Image.open("11d@2x.png"))

    elif Code < 400:
        icon = ImageTk.PhotoImage(Image.open("09d@2x.png"))

    elif Code < 510 and (Hour <= 18 or Hour >= 7):
        icon = ImageTk.PhotoImage(Image.open("10d@2x.png"))

    elif Code < 510 and (Hour >= 19 or Hour <= 6):
        icon = ImageTk.PhotoImage(Image.open("10n@2x.png"))

    elif Code < 600:
        icon = ImageTk.PhotoImage(Image.open("09d@2x.png"))

    elif Code < 800:
        icon = ImageTk.PhotoImage(Image.open("50d@2x.png"))

    elif Code == 800 and (Hour <= 18 or Hour >= 7):
        icon = ImageTk.PhotoImage(Image.open("01d@2x.png"))

    elif Code == 800 and (Hour >= 19 or Hour <= 6):
        icon = ImageTk.PhotoImage(Image.open("01n@2x.png"))

    elif Code == 801 and (Hour <= 18 or Hour >= 7):
        icon = ImageTk.PhotoImage(Image.open("02d@2x.png"))

    elif Code == 801 and (Hour >= 19 or Hour <= 6):
        icon = ImageTk.PhotoImage(Image.open("02n@2x.png"))

    elif Code == 802 and (Hour <= 18 or Hour >= 7):
        icon = ImageTk.PhotoImage(Image.open("03d@2x.png"))

    elif Code == 802 and (Hour >= 19 or Hour <= 6):
        icon = ImageTk.PhotoImage(Image.open("03n@2x.png"))

    elif Code < 810:
        icon = ImageTk.PhotoImage(Image.open("04d@2x.png"))

    weather.config(image = icon)
    Temperature.config(text = '{}°C'.format(temp))
    forecast.config(text = description)


    window.after(10000,getWeather)


title = Label(weatherWidget, text='Singapore', font=("Helvetica", 20), bg="black", fg="white")
weather = Label(weatherWidget, image= '', bg="black")
Temperature = Label(weatherWidget, text = '' , font=("Helvetica", 40), bg="black", fg="white")
forecast = Label(weatherWidget, text= '', font=("Helvetica", 15), bg="black", fg="white")

title.grid(column = 0, row = 0)
weather.grid( column = 0, row = 1)
Temperature.grid( column = 0, row = 2 )
forecast.grid(column = 0, row = 3)

time()
getWeather()
data()

#window.attributes("-fullscreen",True)
window.bind("<Escape>", exit)
window.mainloop()