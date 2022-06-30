from time import sleep
from turtle_racer import TurtleRacer


def run():
    """Turtle Racer."""
    run = TurtleRacer()

    # Display screen.
    run.create_screen()
    # Display heading.
    run.draw_heading()

    while True:

        while True:
            # Display track.
            run.draw_track()
            # Display finish line.
            run.draw_finish_line()

            # Create turtle racers.
            red = run.create_turtle("red", -510, 215)
            orange = run.create_turtle("orange", -510, 165)
            yellow = run.create_turtle("yellow", -510, 115)
            lime = run.create_turtle("lime", -510, 65)
            green = run.create_turtle("green", -510, 15)
            cyan = run.create_turtle("cyan", -510, -35)
            blue = run.create_turtle("blue", -510, -85)
            purple = run.create_turtle("purple", -510, -135)
            magenta = run.create_turtle("magenta", -510, -185)
            pink = run.create_turtle("pink", -510, -235)

            # Display available color options.
            run.display_available_options()
            # Requesting user input.
            racer = run.select_turtle()
            # Requesting user input.
            bet = run.place_bet()

            # Pause for a second.
            sleep(1)

            # Starting the race.
            run.start_race(
                red, orange, yellow, lime, green, cyan, blue, purple, magenta, pink
            )
            # Winning turtle conditions.
            winner = run.win_condition(
                red, orange, yellow, lime, green, cyan, blue, purple, magenta, pink
            )
            # Winning turtle bet conditions.
            run.bet_condition(winner, racer, bet)
            # Display available credits.
            run.display_available_credits()
            # Verify available credits.
            if run.verify_available_credits() == True:
                break
            else:
                continue

        # Requesting user input.
        run.restart()

        continue


if __name__ == "__main__":
    run()
