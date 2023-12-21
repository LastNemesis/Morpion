## Import main library
from tkinter import *

## Importing the files
from src.board import Board
from src.game_logic import Game
#from src.player import player


## Main function
def main():
    """ Main function """

    # Intializing game logic
    brain = Game(0, 0, 0)
    
    # Intializing the Board
    board = Board(brain)

    # Re-Intializing the game logic parameters
    brain.board = board
    brain.width = board.width
    brain.height = board.height

    # Starting the mainloop
    board.start()

## Call the main function to start the application
if __name__ == "__main__":
    main()