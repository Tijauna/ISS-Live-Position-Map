#importing modules
import turtle
import json
import urllib2
from time import sleep

url = "http://api.open-notify.org/iss-now.json"
data = json.load(urllib2.urlopen(url))
time = float(data['timestamp'])

datalist = data['iss_position']
latitude = float(datalist['latitude'])
longitude = float(datalist['longitude'])
turtle.penup()
turtle.setx(latitude)
turtle.sety(longitude)

t2 = turtle.Turtle()

t3 = turtle.Turtle()

screen = turtle.Screen()
screen.setup(1024,512)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('map_earth_bkg.gif')
image = "ISS.gif"

screen.addshape(image)
turtle.shape(image)

#get the ISS position data
while (time < (time + 3600)):
    url = "http://api.open-notify.org/iss-now.json"
    data = json.load(urllib2.urlopen(url))

    time = float(data['timestamp'])
    datalist = data['iss_position']
    latitude = float(datalist['latitude'])
    longitude = float(datalist['longitude'])


    turtle.penup()
    turtle.setx(longitude)
    turtle.sety(latitude)

    t2.penup()
    t2.setx(-180)
    t2.sety(85)
    t2.write(latitude)

    t3.penup()
    t3.setx(-180)
    t3.sety(78)
    t3.write(longitude)
    

    sleep(1)
    t2.clear()
    t3.clear()
