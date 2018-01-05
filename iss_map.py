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


screen = turtle.Screen()
screen.setup(1024,478)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('map_earth_bkg.gif')

#get the ISS position data
while (time < (time + 3600)):
    url = "http://api.open-notify.org/iss-now.json"
    data = json.load(urllib2.urlopen(url))

    time = float(data['timestamp'])
    datalist = data['iss_position']
    latitude = float(datalist['latitude'])
    longitude = float(datalist['longitude'])

    print latitude
    print longitude
    turtle.penup()
    turtle.setx(latitude)
    turtle.sety(longitude)

    sleep(1)
