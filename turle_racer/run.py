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

    # Create turtle racers.
    red = run.turtle_red()
    orange = run.turtle_orange()
    yellow = run.turtle_yellow()
    lime = run.turtle_lime()
    green = run.turtle_green()
    cyan = run.turtle_cyan()
    blue = run.turtle_blue()
    purple = run.turtle_purple()
    magenta = run.turtle_magenta()
    pink = run.turtle_pink()

    # Pause for a second.
    time.sleep(1)

    # Starting the race.
    run.race(red, orange, yellow, lime, green,
             cyan, blue, purple, magenta, pink)
    # Win conditions.
    run.win_condition(red, orange, yellow, lime, green,
                      cyan, blue, purple, magenta, pink)


if __name__ == '__main__':
    run()
