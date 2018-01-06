#importing modules
import turtle
import json
import urllib2
from time import sleep

try:
    url = "http://api.open-notify.org/iss-now.json"
    data = json.load(urllib2.urlopen(url))


except:
    print ('Error: Could not update. Connection Lost.')
    exit()
    
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
screen.setup(905,452)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('map_earth_bkg.gif')
image = "ISS.gif"

screen.addshape(image)
turtle.shape(image)

connection = True

#get the ISS position data
while (connection == True):
    try:
        
        url = "http://api.open-notify.org/iss-now.json"
        data = json.load(urllib2.urlopen(url))
    except:
        connection = False
        print ('Error: Could not update. Connection Lost.')
        exit()

    time = float(data['timestamp'])
    datalist = data['iss_position']
    latitude = float(datalist['latitude'])
    longitude = float(datalist['longitude'])


    turtle.penup()
    turtle.setx(longitude)
    turtle.sety(latitude)

    t2.penup()
    t2.hideturtle()
    t2.setx(-130)
    t2.sety(-71)
     
    t2.write(latitude,font=("Agency FB", 8, "bold"))

    t3.penup()
    t3.hideturtle()
    t3.setx(-130)
    t3.sety(-77)
    
    t3.write(longitude,font=("Agency FB", 8, "bold"))
    

    sleep(1)
    t2.clear()
    t3.clear()
