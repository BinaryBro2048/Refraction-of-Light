#Importing Modules
from turtle import *
from math import *

#Screen
wn = Screen()
wn.screensize(400, 400)
wn.bgcolor("black")
wn.title("Refraction of Light")

#Light Ray(Turtle)
body = Turtle()
body.penup()
body.goto(0, 100)
body.color("white")
body.width(2)
body.setheading(90)


#Surface Set-Up Function
def set_up_surface(color, width):
    s = Turtle()
    s.penup()
    s.speed(0)
    s.goto(-400, 0)
    s.pendown()
    s.color(color)
    s.width(width)
    s.goto(400, 0)
    s.penup()
    s.color("black")

#Declaring Dicts and Lists
media_dict = {"Vacuum":1, "Air":1.003, "Water":1.333, "Glass":1.52, "Diamond":2.42}
colors_dict = {"White":1, "Red":0.7, "Orange":0.59, "Yellow":0.57, "Green":0.495, "Blue":0.45, "Indigo":0.42, "Violet":0.38}
const_dict = {"Vacuum":1, "Air":0.000057, "Water":0.003, "Glass":0.0042, "Diamond":0.013}
speed_dict = {"Vacuum":9, "Air":3, "Water":2, "Glass":2, "Diamond":1}
colors = list(colors_dict.keys())
media = list(media_dict.keys())

#Input Color
print("Please enter the color of light:")
for i in range(0, len(colors)):
    print("{idx}. {color}".format(idx = i + 1, color = colors[i]))
col = input()

#Input Media
print("Please enter the medium from which the light arrives:")
for i in range(0, len(media)):
    print("{idx}. {medium}".format(idx = i+1, medium = media[i]))

med1 = input()
spd1 = speed_dict[med1]
if col == "White" or med1 == "Vacuum":
    ref1 = media_dict[med1]
else:
    ref1 = media_dict[med1] + (const_dict[med1]/(colors_dict[col]*colors_dict[col]))

media.remove(med1)

print("Please enter the medium which the light enters:")
for i in range(0, len(media)):
    print("{idx}. {medium}".format(idx = i+1, medium = media[i]))

med2 = input()
spd2 = speed_dict[med2]
if col == "White" or med2 == "Vacuum":
    ref2 = media_dict[med2]
else:
    ref2 = media_dict[med2] + (const_dict[med2]/(colors_dict[col]*colors_dict[col]))

#Input Angle of Incidence
aoi = int(input("Please enter the angle of incidence:"))

#Trig Functions to Accept Values in Degrees
def sind(angle):
    return degrees(sin(radians(angle)))

def asind(value):
    return degrees(asin(radians(value)))

#Angle of Refraction and Critical Angle Calculation
try:   
    aor = asind((ref1 * sind(aoi))/ref2)
except:
    pass

crit = floor(degrees(asin(radians(ref2)/radians(ref1))))

if aoi == crit:
    aor = 90


#Program Loop
set_up_surface("white", 5)
body.color(col.lower())
body.right(aoi - 180)
body.setx((body.xcor() + aoi)*4)
body.sety(body.ycor() - aoi)
body.speed(spd1)
body.pendown()
can_reverse = False

while body.ycor() > 0: #Before Hitting Surface
    body.fd(2)

if ref1 > ref2 and aoi <= crit: #Denser to Rarer and no TOI
    body.right(aor-aoi)
elif ref1 > ref2 and aoi > crit: #Denser to Rarer with TOI
    body.right((90-aoi)*2)
    can_reverse = True
elif ref2 > ref1: #Rarer to Denser
    body.left(aoi-aor)
    body.speed(spd2)

while body.ycor() <= 0 or can_reverse == True and body.ycor() > -400: #After Hitting Surface/TOI
    body.fd(2)
