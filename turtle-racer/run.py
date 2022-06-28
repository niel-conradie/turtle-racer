from time import sleep
from turtle_racer import TurtleRacer


def run():
    """ Turtle Racer """
    run = TurtleRacer()

    # Display screen.
    run.create_screen()
    # Display heading.
    run.draw_heading()

    while True:
        # Display track.
        run.draw_track()
        # Display finish line.
        run.draw_finish_line()

        # Create turtle racers.
        red = run.create_turtle('red', -510, 215)
        orange = run.create_turtle('orange', -510, 165)
        yellow = run.create_turtle('yellow', -510, 115)
        lime = run.create_turtle('lime', -510, 65)
        green = run.create_turtle('green', -510, 15)
        cyan = run.create_turtle('cyan', -510, -35)
        blue = run.create_turtle('blue', -510, -85)
        purple = run.create_turtle('purple', -510, -135)
        magenta = run.create_turtle('magenta', -510, -185)
        pink = run.create_turtle('pink', -510, -235)

        # Display color options.
        run.display_options()
        # Requesting user input.
        racer = run.select_turtle()
        # Requesting user input.
        amount = run.place_bet()

        # Pause for a second.
        sleep(1)

        # Starting the race.
        run.race(red, orange, yellow, lime, green,
                 cyan, blue, purple, magenta, pink)
        # Winning turtle conditions.
        winner = run.win_condition(
            red, orange, yellow, lime, green, cyan, blue, purple, magenta, pink)
        # Winning turtle bet conditions.
        run.bet_condition(winner, racer, amount)
        # Display available credits.
        run.display_credits()
        # Verify available credits.
        run.check_credits()
        # Requesting user input.
        run.restart()

        continue


if __name__ == '__main__':
    run()
