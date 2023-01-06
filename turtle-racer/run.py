from turtle_racer import TurtleRacer


if __name__ == "__main__":
    run = TurtleRacer()

    try:
        # Starting the game.
        run.start_game()
    except KeyboardInterrupt:
        # Stopping the game.
        quit("\nProgram Terminated")
