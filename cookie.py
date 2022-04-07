#Python 3.x compatitable
import turtle

#screen
wn = turtle.Screen()
wn.title('Cookie Clicker By @Exo.')
wn.bgcolor("red")

#creating the cookie
wn.register_shape("cookie.gif") #register the shape

cookie = turtle.Turtle()
wn.shape("cookie.gif") #Note that by default, turtle places the images on top of the screen,ill add this image on the github 
cookie.speed(0)

clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 400) #x and y coordinates
pen.write(f"Clicks: {clicks}", align ="center", font = ("Courier New", 32, "normal"))

#creating a function for clicks
def clicked(x, y): #takes 2 arguments passed by onclick function
	global clicks #change clicks when clicked
	clicks += 1 
	pen.clear()
	pen.write(f"Clicks: {clicks}", align ="center", font = ("Courier New", 32, "normal"))

cookie.onclick(clicked)
	
	

wn.mainloop()
