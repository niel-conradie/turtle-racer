from sys import exit

from turtle_racer import TurtleRacer


def run():
    """Turtle Racer."""
    run = TurtleRacer()

    try:
        # Starting the game.
        run.start_game()
    except KeyboardInterrupt:
        # Stopping the game.
        exit("\nProgram Terminated")


if __name__ == "__main__":
    run()
