import turtle
import time
import random

posp = 0.1
 
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)


#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Snake eat
eat = turtle.Turtle()
eat.speed(0)
eat.shape("circle")
eat.color("red")
eat.penup()
eat.goto(0,50)

#Functions

def up():
    head.direction = "up"
    
def down():
    head.direction = "down"
    
def left():
    head.direction = "left"
    
def right():
    head.direction = "right"
    
def mov():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#Ketboard
wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(right, "Right")
wn.onkeypress(left, "Left")

while True:
    wn.update()
    
    if head.distance(eat) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        eat.goto(x, y)
    
    mov()
    time.sleep(posp)
    





wn.mainloop()