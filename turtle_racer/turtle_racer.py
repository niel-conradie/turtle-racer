import turtle
import random


class TurtleRacer:
    """ A class to represent a Turtle Racer game. """

    @staticmethod
    def create_screen():
        """ Display screen. """
        screen = turtle.Screen()
        screen.setup(width=1280, height=720, startx=None, starty=None)
        screen.title("Turtle Racer")
        screen.bgcolor('forestgreen')
        return screen

    @staticmethod
    def draw_heading():
        """ Display heading. """
        turtle.speed(0)
        turtle.penup()
        turtle.goto(-100, 275)
        turtle.color('white')
        turtle.write("Turtle Racer", align='left', font=('Arial', 30, 'bold'))

    @staticmethod
    def draw_track():
        """ Display track. """
        turtle.goto(-525, 250)
        turtle.pendown()
        turtle.color('chocolate')
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(1050)
            turtle.right(90)
            turtle.forward(520)
            turtle.right(90)
        turtle.end_fill()

    @staticmethod
    def draw_finish_line():
        """ Display finish line. """
        # Finish line.
        square_size = 20
        turtle.shape('square')
        turtle.penup()

        # White squares row 1.
        turtle.color('white')
        for i in range(13):
            turtle.goto(495, (240 - (i * square_size * 2)))
            turtle.stamp()

        # White square row 2.
        for i in range(13):
            turtle.goto(495 + square_size, (240 - square_size) -
                        (i * square_size * 2))
            turtle.stamp()

        # Black square row 1.
        turtle.color('black')
        for i in range(13):
            turtle.goto(495, (220 - (i * square_size * 2)))
            turtle.stamp()

        # Black square row 2.
        for i in range(13):
            turtle.goto(495 + square_size, (260 - square_size) -
                        (i * square_size * 2))
            turtle.stamp()

    @staticmethod
    def turtle_red():
        """ Create a red turtle. """
        red = turtle.Turtle()
        red.color('red')
        red.shape('turtle')
        red.shapesize(1.75)
        red.pensize(5)
        red.speed(7.5)
        red.penup()
        red.goto(-510, 215)
        red.pendown()
        return red

    @staticmethod
    def turtle_orange():
        """ Create a orange turtle. """
        orange = turtle.Turtle()
        orange.color('orange')
        orange.shape('turtle')
        orange.shapesize(1.75)
        orange.pensize(5)
        orange.speed(7.5)
        orange.penup()
        orange.goto(-510, 165)
        orange.pendown()
        return orange

    @staticmethod
    def turtle_yellow():
        """ Create a yellow turtle. """
        yellow = turtle.Turtle()
        yellow.color('yellow')
        yellow.shape('turtle')
        yellow.shapesize(1.75)
        yellow.pensize(5)
        yellow.speed(7.5)
        yellow.penup()
        yellow.goto(-510, 115)
        yellow.pendown()
        return yellow

    @staticmethod
    def turtle_lime():
        """ Create a lime turtle. """
        lime = turtle.Turtle()
        lime.color('lime')
        lime.shape('turtle')
        lime.shapesize(1.75)
        lime.pensize(5)
        lime.speed(7.5)
        lime.penup()
        lime.goto(-510, 65)
        lime.pendown()
        return lime

    @staticmethod
    def turtle_green():
        """ Create a green turtle. """
        green = turtle.Turtle()
        green.color('green')
        green.shape('turtle')
        green.shapesize(1.75)
        green.pensize(5)
        green.speed(7.5)
        green.penup()
        green.goto(-510, 15)
        green.pendown()
        return green

    @staticmethod
    def turtle_cyan():
        """ Create a cyan turtle. """
        cyan = turtle.Turtle()
        cyan.color('cyan')
        cyan.shape('turtle')
        cyan.shapesize(1.75)
        cyan.pensize(5)
        cyan.speed(7.5)
        cyan.penup()
        cyan.goto(-510, -35)
        cyan.pendown()
        return cyan

    @staticmethod
    def turtle_blue():
        """ Create a blue turtle. """
        blue = turtle.Turtle()
        blue.color('blue')
        blue.shape('turtle')
        blue.shapesize(1.75)
        blue.pensize(5)
        blue.speed(7.5)
        blue.penup()
        blue.goto(-510, -85)
        blue.pendown()
        return blue

    @staticmethod
    def turtle_purple():
        """ Create a purple turtle. """
        purple = turtle.Turtle()
        purple.color('purple')
        purple.shape('turtle')
        purple.shapesize(1.75)
        purple.pensize(5)
        purple.speed(7.5)
        purple.penup()
        purple.goto(-510, -135)
        purple.pendown()
        return purple

    @staticmethod
    def turtle_magenta():
        """ Create a magenta turtle. """
        magenta = turtle.Turtle()
        magenta.color('magenta')
        magenta.shape('turtle')
        magenta.shapesize(1.75)
        magenta.pensize(5)
        magenta.speed(7.5)
        magenta.penup()
        magenta.goto(-510, -185)
        magenta.pendown()
        return magenta

    @staticmethod
    def turtle_pink():
        """ Create a pink turtle. """
        pink = turtle.Turtle()
        pink.color('pink')
        pink.shape('turtle')
        pink.shapesize(1.75)
        pink.pensize(5)
        pink.speed(7.5)
        pink.penup()
        pink.goto(-510, -235)
        pink.pendown()
        return pink

    @staticmethod
    def race(red, orange, yellow, lime, green, cyan, blue, purple, magenta, pink):
        """ Start the race. """
        while red.xcor() <= 450 and orange.xcor() <= 450 and \
                yellow.xcor() <= 450 and lime.xcor() <= 450 and \
                green.xcor() <= 450 and cyan.xcor() <= 450 and \
                blue.xcor() <= 450 and purple.xcor() <= 450 and \
                magenta.xcor() <= 450 and pink.xcor() <= 450:
            # Move turtles forward at random speed.
            red.forward(random.randint(5, 15))
            orange.forward(random.randint(5, 15))
            yellow.forward(random.randint(5, 15))
            lime.forward(random.randint(5, 15))
            green.forward(random.randint(5, 15))
            cyan.forward(random.randint(5, 15))
            blue.forward(random.randint(5, 15))
            purple.forward(random.randint(5, 15))
            magenta.forward(random.randint(5, 15))
            pink.forward(random.randint(5, 15))

    @staticmethod
    def win_condition(red, orange, yellow, lime, green, cyan, blue, purple, magenta, pink):
        """ Win conditional statements. """
        # Red turtle wins.
        if red.xcor() > orange.xcor() and red.xcor() > yellow.xcor() and \
                red.xcor() > lime.xcor() and red.xcor() > green.xcor() and \
                red.xcor() > cyan.xcor() and red.xcor() > blue.xcor() and \
                red.xcor() > purple.xcor() and red.xcor() > magenta.xcor() and \
                red.xcor() > pink.xcor():
            print("Red Turtle Wins!")
            for i in range(72):
                red.right(5)
                red.shapesize(3)

        # Orange turtle wins.
        if orange.xcor() > yellow.xcor() and orange.xcor() > lime.xcor() and \
                orange.xcor() > green.xcor() and orange.xcor() > cyan.xcor() and \
                orange.xcor() > blue.xcor() and orange.xcor() > purple.xcor() and \
                orange.xcor() > magenta.xcor() and orange.xcor() > pink.xcor() and \
                orange.xcor() > red.xcor():
            print("Orange Turtle Wins!")
            for i in range(72):
                orange.right(5)
                orange.shapesize(3)

        # Yellow turtle wins.
        if yellow.xcor() > lime.xcor() and yellow.xcor() > green.xcor() and \
                yellow.xcor() > cyan.xcor() and yellow.xcor() > blue.xcor() and \
                yellow.xcor() > purple.xcor() and yellow.xcor() > magenta.xcor() and \
                yellow.xcor() > pink.xcor() and yellow.xcor() > red.xcor() and \
                yellow.xcor() > orange.xcor():
            print("Yellow Turtle Wins!")
            for i in range(72):
                yellow.right(5)
                yellow.shapesize(3)

        # Lime turtle wins.
        if lime.xcor() > green.xcor() and lime.xcor() > cyan.xcor() and \
                lime.xcor() > blue.xcor() and lime.xcor() > purple.xcor() and \
                lime.xcor() > magenta.xcor() and lime.xcor() > pink.xcor() and \
                lime.xcor() > red.xcor() and lime.xcor() > orange.xcor() and \
                lime.xcor() > yellow.xcor():
            print("Lime Turtle Wins!")
            for i in range(72):
                lime.right(5)
                lime.shapesize(3)

        # Green turtle wins.
        if green.xcor() > cyan.xcor() and green.xcor() > blue.xcor() and \
                green.xcor() > purple.xcor() and green.xcor() > magenta.xcor() and \
                green.xcor() > pink.xcor() and green.xcor() > red.xcor() and \
                green.xcor() > orange.xcor() and green.xcor() > yellow.xcor() and \
                green.xcor() > lime.xcor():
            print("Green Turtle Wins!")
            for i in range(72):
                green.right(5)
                green.shapesize(3)

        # Cyan turtle wins.
        if cyan.xcor() > blue.xcor() and cyan.xcor() > purple.xcor() and \
                cyan.xcor() > magenta.xcor() and cyan.xcor() > pink.xcor() and \
                cyan.xcor() > red.xcor() and cyan.xcor() > orange.xcor() and \
                cyan.xcor() > yellow.xcor() and cyan.xcor() > lime.xcor() and \
                cyan.xcor() > green.xcor():
            print("Cyan Turtle Wins!")
            for i in range(72):
                cyan.right(5)
                cyan.shapesize(3)

        # Blue turtle wins.
        if blue.xcor() > purple.xcor() and blue.xcor() > magenta.xcor() and \
                blue.xcor() > pink.xcor() and blue.xcor() > red.xcor() and \
                blue.xcor() > orange.xcor() and blue.xcor() > yellow.xcor() and \
                blue.xcor() > lime.xcor() and blue.xcor() > green.xcor() and \
                blue.xcor() > cyan.xcor():
            print("Blue Turtle Wins!")
            for i in range(72):
                blue.right(5)
                blue.shapesize(3)

        # Purple turtle wins.
        if purple.xcor() > magenta.xcor() and purple.xcor() > pink.xcor() and \
                purple.xcor() > red.xcor() and purple.xcor() > orange.xcor() and \
                purple.xcor() > yellow.xcor() and purple.xcor() > lime.xcor() and \
                purple.xcor() > green.xcor() and purple.xcor() > cyan.xcor() and \
                purple.xcor() > blue.xcor():
            print("Purple Turtle Wins!")
            for i in range(72):
                purple.right(5)
                purple.shapesize(3)

        # Magenta turtle wins.
        if magenta.xcor() > pink.xcor() and magenta.xcor() > red.xcor() and \
                magenta.xcor() > orange.xcor() and magenta.xcor() > yellow.xcor() and \
                magenta.xcor() > lime.xcor() and magenta.xcor() > green.xcor() and \
                magenta.xcor() > cyan.xcor() and magenta.xcor() > blue.xcor() and \
                magenta.xcor() > purple.xcor():
            print("Magenta Turtle Wins!")
            for i in range(72):
                magenta.right(5)
                magenta.shapesize(3)

        # Pink turtle wins.
        if pink.xcor() > red.xcor() and pink.xcor() > orange.xcor() and \
                pink.xcor() > yellow.xcor() and pink.xcor() > lime.xcor() and \
                pink.xcor() > green.xcor() and pink.xcor() > cyan.xcor() and \
                pink.xcor() > blue.xcor() and pink.xcor() > purple.xcor() and \
                pink.xcor() > magenta.xcor():
            print("Pink Turtle Wins!")
            for i in range(72):
                pink.right(5)
                pink.shapesize(3)
