import turtle
from turtle import Turtle, Screen
from math import pi, sin, cos
import json
import urllib2

def motion():
    global n, t
    turtle.setposition(x_pos(t), y_pos(t))
    longitudeDisplay.write
    t = t+1
    time_t.undo()  # undraw the last time update
    time_t.write("Refreshes: "+ str(t), font=("Agency FB", 8, "bold"))  # Show the time variable t on screen
    longitudeDisplay.undo()
    longitudeDisplay.write(x_pos(t), font=("Agency FB", 8, "bold"))
    latitudeDisplay.undo()
    latitudeDisplay.write(y_pos(t), font=("Agency FB", 8, "bold"))
    velocityDisplay.undo()
    velocityDisplay.write("Velocity: "+ str(round(otherData(t)[0],2))+" km/h", font=("Agency FB", 8, "bold"))
    altitudeDisplay.undo()
    altitudeDisplay.write("Altitude: "+ str(round(otherData(t)[1],2))+" km", font=("Agency FB", 8, "bold"))
    visibilityDisplay.undo()
    visibilityDisplay.write("Visibility: "+ str(otherData(t)[2]), font=("Agency FB", 8, "bold"))


    screen.update()
	
    n = n + 1
    screen.ontimer(motion, 100)

def otherData(t):
    try:
	url = "https://api.wheretheiss.at/v1/satellites/25544"
	data = json.load(urllib2.urlopen(url))
    except:
	exit()
    
    velocity = float(data['velocity'])
    altitude = float(data['altitude'])
    visibility = data['visibility']
    return [velocity, altitude, visibility]    

def x_pos(t):
    try:

        url = "http://api.open-notify.org/iss-now.json"
        data = json.load(urllib2.urlopen(url))
    except:
	exit()

    datalist = data['iss_position']
    latitude = float(datalist['latitude'])
    longitude = float(datalist['longitude'])
    return longitude

def y_pos(t):

    try:

        url = "http://api.open-notify.org/iss-now.json"
        data = json.load(urllib2.urlopen(url))
    except:
	exit()

    datalist = data['iss_position']
    latitude = float(datalist['latitude'])
    longitude = float(datalist['longitude'])
    return latitude

n = t = 0

screen = turtle.Screen()
screen.setup(905,452)
screen.tracer(0)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('map_earth_bkg.gif')
screen.tracer(0)  # Control animation updates ourself

image = "ISS.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()
turtle.setposition(x_pos(t), y_pos(t))
turtle.pendown()
turtle.showturtle()

latitude = x_pos(t)
latitudeDisplay = Turtle(visible=False)  # For latitude output
latitudeDisplay.penup()
latitudeDisplay.setposition(-130, -71) 
latitudeDisplay.write(latitude, font=("Agency FB", 8, "bold"))

longitude = y_pos(t)
longitudeDisplay = Turtle(visible=False)  # For longitude output
longitudeDisplay.penup()
longitudeDisplay.setposition(-130, -77) 
longitudeDisplay.write(longitude, font=("Agency FB", 8, "bold"))

time_t = Turtle(visible=False)  # For time output
time_t.penup()
time_t.setposition(100, -71)  
time_t.write("Refreshes: " + str(t), font=("Agency FB", 8, "bold")) 

velocity = otherData(t)[0]
velocityDisplay = Turtle(visible=False)  
velocityDisplay.penup()
velocityDisplay.setposition(40, -77)
velocityDisplay.write("Velocity: ", velocity, font=("Agency FB", 8, "bold"))

altitude = otherData(t)[1]
altitudeDisplay = Turtle(visible=False)  
altitudeDisplay.penup()
altitudeDisplay.setposition(40, -71)
altitudeDisplay.write("Altitude: ", altitude, font=("Agency FB", 8, "bold"))

visibility = otherData(t)[2]
visibilityDisplay = Turtle(visible=False)  
visibilityDisplay.penup()
visibilityDisplay.setposition(100, -77)
visibilityDisplay.write("Visibility: ", visibility, font=("Agency FB", 8, "bold"))


screen.ontimer(motion, 100)

screen.exitonclick()
