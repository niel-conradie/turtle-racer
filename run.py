import time

from turtle_racer import TurtleRacer


def run():
    """ Turtle Racer """
    run = TurtleRacer()

    # Display screen.
    run.create_screen()
    # Display heading.
    run.draw_heading()
    # Display track.
    run.draw_track()
    # Display finish line.
    run.draw_finish_line()

    # Create blue turtle.
    blue = run.turtle_blue()
    pink = run.turtle_pink()
    yellow = run.turtle_yellow()
    green = run.turtle_green()

    # Pause for a second.
    time.sleep(1)

    # Starting the race.
    run.race(blue, pink, yellow, green)
    # Win conditions.
    run.win_condition(blue, pink, yellow, green)


if __name__ == '__main__':
    run()
