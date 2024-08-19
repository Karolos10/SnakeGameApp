import turtle
import time
import random

posp = 0.1
 
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Score
score = 0
high_score = 0

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake eat
eat = turtle.Turtle()
eat.speed(0)
eat.shape("circle")
eat.color("red")
eat.penup()
eat.goto(0, 50)

# Segments / Body of the snake
segments = []

# Texts
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0, 260)
text.write("Score: 0     High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions


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


# Ketboard
wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(right, "Right")
wn.onkeypress(left, "Left")

while True:
    wn.update()
    
    # Colision borders
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        
        # Change segments position
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Crear segmentos
        segments.clear()
        
        # Reset score
        score = 0
        text.clear()    
        text.write("Score: {}     High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    
    if head.distance(eat) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        eat.goto(x, y)
        
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)
        
        # Increase score
        score += 10
        
        if score > high_score:
            high_score = score
        
        text.clear()    
        text.write("Score: {}     High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    
    # Moving the snake's body
    totalSeg = len(segments)
    for index in range(totalSeg - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    
    if totalSeg > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    
    mov()
    
    # Colision with the body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            
            for segment in segments:
                segment.goto(1000, 1000)
            
            segments.clear()
            
            score = 0
            text.clear()    
            text.write("Score: {}     High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    
    time.sleep(posp)

wn.mainloop()
