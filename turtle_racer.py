import turtle
import random
import time


# Display screen.
screen = turtle.Screen()
screen.setup(width=800, height=500, startx=None, starty=None)
screen.title("Turtle Racer")
screen.bgcolor('forestgreen')

# Display heading.
turtle.speed(0)
turtle.penup()
turtle.goto(-100, 205)
turtle.color('white')
turtle.write("Turtle Racer", align='left', font=('Arial', 20, 'bold'))

# Display track.
turtle.goto(-350, 200)
turtle.pendown()
turtle.color('chocolate')
turtle.begin_fill()
for i in range(2):
    turtle.forward(700)
    turtle.right(90)
    turtle.forward(400)
    turtle.right(90)
turtle.end_fill()

# Display finish line.
# Finish line.
square_size = 20
turtle.shape('square')
turtle.penup()

# White squares row 1.
turtle.color('white')
for i in range(10):
    turtle.goto(250, (170 - (i * square_size * 2)))
    turtle.stamp()

# White square row 2.
for i in range(10):
    turtle.goto(250 + square_size, (210 - square_size) - (i * square_size * 2))
    turtle.stamp()

# Black square row 1.
turtle.color('black')
for i in range(10):
    turtle.goto(250, (190 - (i * square_size * 2)))
    turtle.stamp()

# Black square row 2.
for i in range(10):
    turtle.goto(251 + square_size, (190 - square_size) - (i * square_size * 2))
    turtle.stamp()

# Create a blue turtle.
blue = turtle.Turtle()
blue.color('cyan')
blue.shape('turtle')
blue.shapesize(1.5)
blue.penup()
blue.goto(-300, 150)
blue.pendown()

# Create a pink turtle.
pink = turtle.Turtle()
pink.color('magenta')
pink.shape('turtle')
pink.shapesize(1.5)
pink.penup()
pink.goto(-300, 50)
pink.pendown()

# Create a yellow turtle.
yellow = turtle.Turtle()
yellow.color('yellow')
yellow.shape('turtle')
yellow.shapesize(1.5)
yellow.penup()
yellow.goto(-300, -50)
yellow.pendown()

# Create a green turtle.
green = turtle.Turtle()
green.color('lime')
green.shape('turtle')
green.shapesize(1.5)
green.penup()
green.goto(-300, -150)
green.pendown()

# Pause for a second.
time.sleep(1)

# Start the race.
while blue.xcor() <= 230 and pink.xcor() <= 230 and yellow.xcor() <= 230 and green.xcor() <= 230:
    blue.forward(random.randint(1, 10))
    pink.forward(random.randint(1, 10))
    yellow.forward(random.randint(1, 10))
    green.forward(random.randint(1, 10))

# Blue turtle wins.
if blue.xcor() > pink.xcor() and blue.xcor() > yellow.xcor() and blue.xcor() > green.xcor():
    print("Blue turtle wins!")
    for i in range(72):
        blue.right(5)
        blue.shapesize(2.5)

# Pink turtle wins.
elif pink.xcor() > yellow.xcor() and pink.xcor() > green.xcor() and pink.xcor() > blue.xcor():
    print("Pink turtle wins!")
    for i in range(72):
        pink.right(5)
        pink.shapesize(2.5)

# Yellow turtle wins.
elif yellow.xcor() > green.xcor() and yellow.xcor() > blue.xcor() and yellow.xcor() > blue.xcor():
    print("Yellow turtle wins!")
    for i in range(72):
        yellow.right(5)
        yellow.shapesize(2.5)

# Green turtle wins.
elif green.xcor() > blue.xcor() and green.xcor() > pink.xcor() and green.xcor() > yellow.xcor():
    print("Green turtle wins!")
    for i in range(72):
        green.right(5)
        green.shapesize(2.5)
