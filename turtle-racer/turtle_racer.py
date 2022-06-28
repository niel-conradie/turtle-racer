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
    def create_turtle(color, x, y):
        """ Create a turtle racer. """
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.shapesize(1.75)
        racer.pensize(5)
        racer.speed(7.5)
        racer.penup()
        racer.goto(x, y)
        racer.pendown()
        return racer

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

    def win_condition(self, red, orange, yellow, lime, green, cyan, blue, purple, magenta, pink):
        """ Win conditional statements. """
        # Red turtle wins.
        if red.xcor() > orange.xcor() and red.xcor() > yellow.xcor() and \
                red.xcor() > lime.xcor() and red.xcor() > green.xcor() and \
                red.xcor() > cyan.xcor() and red.xcor() > blue.xcor() and \
                red.xcor() > purple.xcor() and red.xcor() > magenta.xcor() and \
                red.xcor() > pink.xcor():

            print("\nRed Turtle Wins!")
            self.celebrate(red)

        # Orange turtle wins.
        if orange.xcor() > yellow.xcor() and orange.xcor() > lime.xcor() and \
                orange.xcor() > green.xcor() and orange.xcor() > cyan.xcor() and \
                orange.xcor() > blue.xcor() and orange.xcor() > purple.xcor() and \
                orange.xcor() > magenta.xcor() and orange.xcor() > pink.xcor() and \
                orange.xcor() > red.xcor():

            print("\nOrange Turtle Wins!")
            self.celebrate(orange)

        # Yellow turtle wins.
        if yellow.xcor() > lime.xcor() and yellow.xcor() > green.xcor() and \
                yellow.xcor() > cyan.xcor() and yellow.xcor() > blue.xcor() and \
                yellow.xcor() > purple.xcor() and yellow.xcor() > magenta.xcor() and \
                yellow.xcor() > pink.xcor() and yellow.xcor() > red.xcor() and \
                yellow.xcor() > orange.xcor():

            print("\nYellow Turtle Wins!")
            self.celebrate(yellow)

        # Lime turtle wins.
        if lime.xcor() > green.xcor() and lime.xcor() > cyan.xcor() and \
                lime.xcor() > blue.xcor() and lime.xcor() > purple.xcor() and \
                lime.xcor() > magenta.xcor() and lime.xcor() > pink.xcor() and \
                lime.xcor() > red.xcor() and lime.xcor() > orange.xcor() and \
                lime.xcor() > yellow.xcor():

            print("\nLime Turtle Wins!")
            self.celebrate(lime)

        # Green turtle wins.
        if green.xcor() > cyan.xcor() and green.xcor() > blue.xcor() and \
                green.xcor() > purple.xcor() and green.xcor() > magenta.xcor() and \
                green.xcor() > pink.xcor() and green.xcor() > red.xcor() and \
                green.xcor() > orange.xcor() and green.xcor() > yellow.xcor() and \
                green.xcor() > lime.xcor():

            print("\nGreen Turtle Wins!")
            self.celebrate(green)

        # Cyan turtle wins.
        if cyan.xcor() > blue.xcor() and cyan.xcor() > purple.xcor() and \
                cyan.xcor() > magenta.xcor() and cyan.xcor() > pink.xcor() and \
                cyan.xcor() > red.xcor() and cyan.xcor() > orange.xcor() and \
                cyan.xcor() > yellow.xcor() and cyan.xcor() > lime.xcor() and \
                cyan.xcor() > green.xcor():

            print("\nCyan Turtle Wins!")
            self.celebrate(cyan)

        # Blue turtle wins.
        if blue.xcor() > purple.xcor() and blue.xcor() > magenta.xcor() and \
                blue.xcor() > pink.xcor() and blue.xcor() > red.xcor() and \
                blue.xcor() > orange.xcor() and blue.xcor() > yellow.xcor() and \
                blue.xcor() > lime.xcor() and blue.xcor() > green.xcor() and \
                blue.xcor() > cyan.xcor():

            print("\nBlue Turtle Wins!")
            self.celebrate(blue)

        # Purple turtle wins.
        if purple.xcor() > magenta.xcor() and purple.xcor() > pink.xcor() and \
                purple.xcor() > red.xcor() and purple.xcor() > orange.xcor() and \
                purple.xcor() > yellow.xcor() and purple.xcor() > lime.xcor() and \
                purple.xcor() > green.xcor() and purple.xcor() > cyan.xcor() and \
                purple.xcor() > blue.xcor():

            print("\nPurple Turtle Wins!")
            self.celebrate(purple)

        # Magenta turtle wins.
        if magenta.xcor() > pink.xcor() and magenta.xcor() > red.xcor() and \
                magenta.xcor() > orange.xcor() and magenta.xcor() > yellow.xcor() and \
                magenta.xcor() > lime.xcor() and magenta.xcor() > green.xcor() and \
                magenta.xcor() > cyan.xcor() and magenta.xcor() > blue.xcor() and \
                magenta.xcor() > purple.xcor():

            print("\nMagenta Turtle Wins!")
            self.celebrate(magenta)

        # Pink turtle wins.
        if pink.xcor() > red.xcor() and pink.xcor() > orange.xcor() and \
                pink.xcor() > yellow.xcor() and pink.xcor() > lime.xcor() and \
                pink.xcor() > green.xcor() and pink.xcor() > cyan.xcor() and \
                pink.xcor() > blue.xcor() and pink.xcor() > purple.xcor() and \
                pink.xcor() > magenta.xcor():

            print("\nPink Turtle Wins!")
            self.celebrate(pink)

    @staticmethod
    def celebrate(turtle):
        """ Winning turtle celebrates. """
        for i in range(72):
            turtle.right(5)
            turtle.shapesize(3)

    @staticmethod
    def restart():
        """ Requesting user input and validating choice. """
        while True:
            user_input = turtle.textinput(
                "Restart", "\nRestart? Yes/No: ").lower()
            choices = ['yes', 'no']
            if user_input not in choices:
                print("\nPlease type 'yes' or 'no'")
                continue

            # User input conditions.
            if user_input == 'yes':
                return
            if user_input == 'no':
                print("\nThank you for playing!")
                quit()
