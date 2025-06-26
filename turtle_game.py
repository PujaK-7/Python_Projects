import turtle # allows us to use the turtles library

window = turtle.Screen() # creates a graphics window
window.setup(500,500) # set window dimension

circle_rad=60 # set the radius
tab=10 #set the tab


kat = turtle.Turtle() # create a turtle named kat
kat.shape("turtle") # kat looks like a turtle
kat.color('green') # kat has a color
kat.circle(circle_rad)
kat.backward(tab)
kat.circle(circle_rad)
kat.backward(tab)
kat.circle(circle_rad)
kat.backward(tab)
kat.circle(circle_rad)
kat.backward(tab)
kat.circle(circle_rad)
#kat.forward(tab*2)
#kat.right(90)
