import sys

from turtle_racer import TurtleRacer


def run():
    """Turtle Racer."""
    run = TurtleRacer()

    try:
        # Starting the game.
        run.start_game()
    except KeyboardInterrupt:
        # Stopping the game.
        sys.exit("\nProgram Terminated")


if __name__ == "__main__":
    run()
